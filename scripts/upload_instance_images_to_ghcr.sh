#!/bin/bash

# Prerequisites
# 
# 1. A Github account (https://github.com)
# 2. A Github personal access token with read/write packages and repo permission (https://github.com/settings/tokens)
# 3. Set environment variables:
#     $ export GH_USERNAME=<your_github_username>
#     $ export GH_PAT=<your_token>
# 4. Run the script (it handles Docker login automatically):
#     $ ./scripts/upload_instance_images_to_ghcr.sh --dry-run --limit 1
#
# Usage:
#     $ ./scripts/upload_instance_images_to_ghcr.sh --jobs 8 --skip-existing --version v1.0
# 
# Important: In order to avoid costs and to enable users to access the images, the uploaded GHCR images must have
# their visibility set to "public". Unfortunately, the only way to do this is via the GitHub web interface, and must be
# done for every single image manually.

set -euo pipefail

# Configuration
DEFAULT_VERSION="v1.0"
DEFAULT_DATASET="AmazonScience/SWE-PolyBench_500"
DEFAULT_REPO_PATH="~/polybench_repos"

# Script options
DRY_RUN=false
VERSION="$DEFAULT_VERSION"
DATASET_PATH="$DEFAULT_DATASET"
REPO_PATH="$DEFAULT_REPO_PATH"
PARALLEL_JOBS=1
SKIP_EXISTING=false
LIMIT=""
OFFSET=""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging functions
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Usage function
usage() {
    cat << EOF
Usage: $0 [OPTIONS]

Build and upload SWE-PolyBench instance images to GitHub Container Registry.

OPTIONS:
    -d, --dataset PATH         Dataset path or HuggingFace path (default: $DEFAULT_DATASET)
    -r, --repo-path PATH       Base repository path (default: $DEFAULT_REPO_PATH)
    -v, --version VERSION      Image version tag (default: $DEFAULT_VERSION)
    -j, --jobs N               Number of parallel jobs (default: 1)
    -l, --limit N              Limit number of instances to process (for testing)
    -o, --offset N             Skip first N instances (for resuming uploads)
    -s, --skip-existing        Skip instances that already have images in registry
    --dry-run                  Perform dry run (build but don't upload)
    -h, --help                 Show this help message

ENVIRONMENT VARIABLES:
    GH_USERNAME                GitHub username (required for GHCR registry)
    GH_PAT                     GitHub personal access token (required for upload)

EXAMPLES:
    # Set up environment (required)
    export GH_USERNAME=your_github_username
    export GH_PAT=your_github_token
    
    # Dry run with default dataset (script handles login automatically)
    $0 --dry-run

    # Test with a single instance (recommended for testing)
    $0 --dry-run --limit 1

    # Resume upload from instance 100 (skip first 100)
    $0 --offset 100 --skip-existing

    # Process instances 50-99 (offset 50, limit 50)
    $0 --offset 50 --limit 50

    # Build and upload with custom dataset
    $0 --dataset /path/to/dataset.csv --version v2.0

    # Parallel processing with 4 jobs
    $0 --jobs 4 --skip-existing

EOF
}

# Parse command line arguments
parse_args() {
    while [[ $# -gt 0 ]]; do
        case $1 in
            -d|--dataset)
                DATASET_PATH="$2"
                shift 2
                ;;
            -r|--repo-path)
                REPO_PATH="$2"
                shift 2
                ;;
            -v|--version)
                VERSION="$2"
                shift 2
                ;;
            -j|--jobs)
                PARALLEL_JOBS="$2"
                shift 2
                ;;
            -l|--limit)
                LIMIT="$2"
                shift 2
                ;;
            -o|--offset)
                OFFSET="$2"
                shift 2
                ;;
            -s|--skip-existing)
                SKIP_EXISTING=true
                shift
                ;;
            --dry-run)
                DRY_RUN=true
                shift
                ;;
            -h|--help)
                usage
                exit 0
                ;;
            *)
                log_error "Unknown option: $1"
                usage
                exit 1
                ;;
        esac
    done
}

# Check prerequisites
check_prerequisites() {
    log_info "Checking prerequisites..."
    
    # Check if GH_USERNAME is set
    if [[ -z "${GH_USERNAME:-}" ]]; then
        log_error "GH_USERNAME environment variable is not set"
        log_error "Please set it with: export GH_USERNAME=<your_github_username>"
        exit 1
    fi
    
    # Set GHCR registry based on username
    GHCR_REGISTRY="ghcr.io/${GH_USERNAME}/swe-polybench.eval.x86_64"
    log_info "Using registry: $GHCR_REGISTRY"
    
    # Check if docker is installed and running
    if ! command -v docker &> /dev/null; then
        log_error "Docker is not installed or not in PATH"
        exit 1
    fi
    
    if ! docker info &> /dev/null; then
        log_error "Docker daemon is not running"
        exit 1
    fi
    
    # Check if GH_PAT is set (required for both Docker login and API calls)
    if [[ -z "${GH_PAT:-}" ]]; then
        log_error "GH_PAT environment variable is not set"
        log_error "This is required for Docker login and setting package visibility to public"
        log_error "Please set it with: export GH_PAT=<your_github_token>"
        exit 1
    fi
    
    # Automatically login to GHCR
    log_info "Logging into GHCR..."
    if ! echo "$GH_PAT" | docker login ghcr.io -u "$GH_USERNAME" --password-stdin &> /dev/null; then
        log_error "Failed to login to GHCR. Please check your GH_PAT token has the required scopes (write:packages, repo)"
        exit 1
    fi
    log_success "Successfully logged into GHCR"
    
    # Check if Python environment is set up
    if ! python3 -c "import poly_bench_evaluation" &> /dev/null; then
        log_error "poly_bench_evaluation package not found. Please install with: pip install -e ."
        exit 1
    fi
    
    log_success "Prerequisites check passed"
}

# Check if image exists in registry
image_exists_in_registry() {
    local instance_id="$1"
    local image_name="${GHCR_REGISTRY}.${instance_id,,}:${VERSION}"
    
    if [[ "$DRY_RUN" == "true" ]]; then
        return 1  # In dry run, assume images don't exist
    fi
    
    # Try to pull the manifest without downloading the image
    if docker manifest inspect "$image_name" &> /dev/null; then
        return 0  # Image exists
    else
        return 1  # Image doesn't exist
    fi
}

# Fix poetry version in langchain instances
fix_poetry_version() {
    local dockerfile="$1"
    local instance_id="$2"

    local langchain_instances=(
        "langchain-ai__langchain-6456"
        "langchain-ai__langchain-6483"
        "langchain-ai__langchain-6765"
    )

    if [[ " ${langchain_instances[@]} " =~ " ${instance_id} " ]]; then
        log_info "Applying poetry version fix for $instance_id" >&2 
        # Update the dockerfile to replace "https://install.python-poetry.org |" with "https://install.python-poetry.org | POETRY_VERSION=1.8.3"
        dockerfile=$(echo "$dockerfile" | sed 's|https://install.python-poetry.org \||https://install.python-poetry.org \| POETRY_VERSION=1.8.3|')
    fi

    echo "$dockerfile"
}

# Fix poetry version in langchain instances
fix_huggingface_model_downloads() {
    local dockerfile="$1"
    local instance_id="$2"

    local hf_instances=(
        "huggingface__transformers-16661"
        "huggingface__transformers-17082"
    )

    if [[ " ${hf_instances[@]} " =~ " ${instance_id} " ]]; then
        log_info "Applying Hugging Face model download fix for $instance_id" >&2
        # Update the dockerfile to add URL fix
        dockerfile=$(echo "$dockerfile" | sed '/COPY . ./a\RUN sed -i '\''s|http_get(url_to_download|http_get("https://huggingface.co" + url_to_download|'\'' src/transformers/utils/hub.py')
    fi

    echo "$dockerfile"
}

# Fix pkg-config missing issue for PyAV build in transformers instances
fix_pkg_config_dockerfile() {
    local dockerfile="$1"
    local instance_id="$2"
    
    # List of instance IDs that need pkg-config fix (from failed_instances.txt)
    local pkg_config_instances=(
        "huggingface__transformers-25358"
        "huggingface__transformers-25765"
        "huggingface__transformers-25884"
        "huggingface__transformers-26164"
        "huggingface__transformers-27463"
        "huggingface__transformers-27561"
        "huggingface__transformers-27717"
        "huggingface__transformers-28010"
        "huggingface__transformers-28517"
        "huggingface__transformers-28522"
        "huggingface__transformers-28535"
        "huggingface__transformers-28563"
        "huggingface__transformers-28940"
    )
    
    # Check if this instance needs the fix
    local needs_fix=false
    for pkg_config_instance in "${pkg_config_instances[@]}"; do
        if [[ "$instance_id" == "$pkg_config_instance" ]]; then
            needs_fix=true
            break
        fi
    done
    
    if [[ "$needs_fix" == "true" ]]; then
        log_info "Applying av version fix for $instance_id" >&2
        # Add pkg-config and pyav dependencies
        dockerfile=$(echo "$dockerfile" | sed 's/build-essential/build-essential pkg-config libavformat-dev libavcodec-dev libavdevice-dev libavutil-dev libswscale-dev libswresample-dev libavfilter-dev/')
        # Pre-install av==10.0.0 and modify setup.py to use compatible version
        dockerfile=$(echo "$dockerfile" | sed '/# Install PyTorch and other dependencies/i\
# Temporarily modify setup.py to replace the problematic av==9.2.0 requirement with av==10.0.0\
RUN sed -i '\''s/\"av==9.2.0\",/\"av==10.0.0\",/g'\'' setup.py\
')
    fi

    echo "$dockerfile"
}

# Fix Debian Buster EOL issues for specific instances
fix_debian_buster_dockerfile() {
    local dockerfile="$1"
    local instance_id="$2"
    
    # List of instance IDs that need Debian Buster archive fix
    local buster_instances=(
        "angular__angular-37561"
        "coder__code-server-4597"
        "coder__code-server-4678"
        "coder__code-server-4923"
        "coder__code-server-5633"
        "coder__code-server-6115"
        "coder__code-server-6225"
        "coder__code-server-6423"
        "huggingface__transformers-6744"
        "huggingface__transformers-7075"
        "huggingface__transformers-7272"
        "huggingface__transformers-7562"
        "huggingface__transformers-8435"
        "microsoft__vscode-118226"
        "microsoft__vscode-122796" 
        "microsoft__vscode-123112"
        "microsoft__vscode-124621"
        "microsoft__vscode-127257"
        "microsoft__vscode-128931"
        "microsoft__vscode-130088"
        "microsoft__vscode-132041"
        "microsoft__vscode-178291"
    )
    
    # Check if this instance needs the fix
    local needs_fix=false
    for buster_instance in "${buster_instances[@]}"; do
        if [[ "$instance_id" == "$buster_instance" ]]; then
            needs_fix=true
            break
        fi
    done
    
    if [[ "$needs_fix" == "true" ]]; then
        log_info "Applying Debian Buster archive fix for $instance_id" >&2
        # Replace debian repositories with archive repositories before apt-get commands
        echo "$dockerfile" | sed 's|RUN apt-get update|RUN sed -i "s/deb.debian.org/archive.debian.org/g" /etc/apt/sources.list \&\& sed -i "s/security.debian.org/archive.debian.org/g" /etc/apt/sources.list \&\& apt-get update|g'
    else
        echo "$dockerfile"
    fi
}

# Fix custom-reporter.js path issues for material-ui instances
fix_custom_reporter_path() {
    local dockerfile="$1"
    local instance_id="$2"
    
    # List of specific material-ui instances that need the custom-reporter.js fix
    # These are the 55 instances with resolved=false (excluding the 6 that already work)
    local mui_instances=(
        "mui__material-ui-7444"
        "mui__material-ui-11446"
        "mui__material-ui-11825"
        "mui__material-ui-12389"
        "mui__material-ui-13582"
        "mui__material-ui-13743"
        "mui__material-ui-13789"
        "mui__material-ui-13828"
        "mui__material-ui-14023"
        "mui__material-ui-14036"
        "mui__material-ui-14266"
        "mui__material-ui-14465"
        "mui__material-ui-15097"
        "mui__material-ui-15430"
        "mui__material-ui-15495"
        "mui__material-ui-16137"
        "mui__material-ui-16882"
        "mui__material-ui-17005"
        "mui__material-ui-17301"
        "mui__material-ui-17640"
        "mui__material-ui-17691"
        "mui__material-ui-17829"
        "mui__material-ui-18744"
        "mui__material-ui-19612"
        "mui__material-ui-19794"
        "mui__material-ui-20133"
        "mui__material-ui-20247"
        "mui__material-ui-20781"
        "mui__material-ui-20851"
        "mui__material-ui-21192"
        "mui__material-ui-21226"
        "mui__material-ui-23174"
        "mui__material-ui-23364"
        "mui__material-ui-25784"
        "mui__material-ui-26173"
        "mui__material-ui-26231"
        "mui__material-ui-26323"
        "mui__material-ui-26460"
        "mui__material-ui-26600"
        "mui__material-ui-26746"
        "mui__material-ui-28813"
        "mui__material-ui-33312"
        "mui__material-ui-34138"
        "mui__material-ui-34158"
        "mui__material-ui-34207"
        "mui__material-ui-34478"
        "mui__material-ui-34548"
        "mui__material-ui-36426"
        "mui__material-ui-37118"
        "mui__material-ui-37845"
        "mui__material-ui-37908"
        "mui__material-ui-38167"
        "mui__material-ui-38788"
        "mui__material-ui-39071"
        "mui__material-ui-40180"
    )
    
    # Check if this instance needs the fix
    local needs_fix=false
    for mui_instance in "${mui_instances[@]}"; do
        if [[ "$instance_id" == "$mui_instance" ]]; then
            needs_fix=true
            break
        fi
    done
    
    # Only apply fix to specific material-ui instances that have custom-reporter.js
    if [[ "$needs_fix" == "true" ]] && [[ "$dockerfile" == *"custom-reporter.js"* ]]; then
        log_info "Applying custom-reporter.js path fix for $instance_id" >&2

        python scripts/fix_custom_reporter_path.py "$dockerfile"
    else
        echo "$dockerfile"
    fi
}

# Build and upload a single instance image
process_instance() {
    local instance_data="$1"
    
    # Parse instance data (JSON format)
    local instance_id=$(echo "$instance_data" | jq -r '.instance_id')
    local language=$(echo "$instance_data" | jq -r '.language')
    local repo=$(echo "$instance_data" | jq -r '.repo')
    local base_commit=$(echo "$instance_data" | jq -r '.base_commit')
    local dockerfile=$(echo "$instance_data" | jq -r '.Dockerfile')
    
    # Apply pkg-config fix if needed
    dockerfile=$(fix_pkg_config_dockerfile "$dockerfile" "$instance_id")
    
    # Apply Debian Buster fix if needed
    dockerfile=$(fix_debian_buster_dockerfile "$dockerfile" "$instance_id")

    # Apply poetry lock file fix if needed
    dockerfile=$(fix_poetry_version "$dockerfile" "$instance_id")

    # Apply HF URL fix
    dockerfile=$(fix_huggingface_model_downloads "$dockerfile" "$instance_id")
    
    # Apply custom-reporter.js path fix if needed
    dockerfile=$(fix_custom_reporter_path "$dockerfile" "$instance_id")
    
    log_info "Processing instance: $instance_id ($language)"
    
    # Check if image already exists and skip if requested
    if [[ "$SKIP_EXISTING" == "true" ]] && image_exists_in_registry "$instance_id"; then
        log_info "Skipping $instance_id - image already exists in registry"
        return 0
    fi
    
    local local_image_name="polybench_${language,,}_${instance_id,,}"
    local remote_image_name="${GHCR_REGISTRY}.${instance_id,,}"
    
    # Create temporary directory for this instance
    local temp_dir=$(mktemp -d)
    local build_log_file="${temp_dir}/build.log"
    
    trap "rm -rf $temp_dir" EXIT
    
    log_info "Building image for $instance_id..."
    
    # Get the directory where this script is located
    local script_dir="${SCRIPT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)}"
    local build_script="${script_dir}/build_instance_image.py"
    
    # Check if the build script exists
    if [[ ! -f "$build_script" ]]; then
        log_error "Build script not found: $build_script"
        return 1
    fi
    
    # Run the build script
    python3 "$build_script" "$instance_id" "$language" "$repo" "$base_commit" "$dockerfile" "$REPO_PATH" 2>&1 | tee "$build_log_file"
    local build_result=${PIPESTATUS[0]}
    
    if [[ $build_result -ne 0 ]]; then
        log_error "Failed to build image for $instance_id"
        cat "$build_log_file"
        return 1
    fi
    
    log_success "Built image for $instance_id"
    
    # Tag and push image (unless dry run)
    if [[ "$DRY_RUN" == "false" ]]; then
        log_info "Tagging and pushing $instance_id..."
        
        # Tag with version and latest
        docker tag "$local_image_name" "${remote_image_name}:${VERSION}"
        docker tag "$local_image_name" "${remote_image_name}:latest"
        
        # Push both tags
        if ! docker push "${remote_image_name}:${VERSION}"; then
            log_error "Failed to push ${remote_image_name}:${VERSION}"
            return 1
        fi
        
        if ! docker push "${remote_image_name}:latest"; then
            log_error "Failed to push ${remote_image_name}:latest"
            return 1
        fi
        
        log_success "Pushed $instance_id to registry"
        
        # Add URL to package settings file for batch processing
        local settings_url="https://github.com/users/${GH_USERNAME}/packages/container/swe-polybench.eval.x86_64.${instance_id,,}/settings"
        echo "$settings_url" >> package_settings_urls.txt
        
        # Note about manual visibility setting
        log_warning "Package uploaded as private. To make it public, visit:"
        log_warning "https://github.com/users/${GH_USERNAME}/packages/container/swe-polybench.eval.x86_64.${instance_id,,}/settings"
    else
        log_info "DRY RUN: Would tag and push $instance_id"
    fi
    
    # Clean up local images to save disk space
    log_info "Cleaning up local images for $instance_id..."
    
    # Remove the original local image
    docker rmi "$local_image_name" &> /dev/null || log_warning "Failed to remove local image $local_image_name"
    
    # Remove the tagged GHCR images (both version and latest)
    docker rmi "${remote_image_name}:${VERSION}" &> /dev/null || log_warning "Failed to remove ${remote_image_name}:${VERSION}"
    docker rmi "${remote_image_name}:latest" &> /dev/null || log_warning "Failed to remove ${remote_image_name}:latest"
    
    # Also clean up base image if it exists and we're not processing more instances
    # (This is a simple cleanup - in practice you might want to keep base images)
    
    log_success "Completed processing $instance_id"
    return 0
}

# Export the function so it can be used by parallel
export -f process_instance
export -f log_info
export -f log_success
export -f log_warning
export -f log_error
export -f image_exists_in_registry
export -f fix_pkg_config_dockerfile
export -f fix_debian_buster_dockerfile
export -f fix_poetry_version
export -f fix_huggingface_model_downloads
export -f fix_custom_reporter_path
export GHCR_REGISTRY VERSION DRY_RUN REPO_PATH SKIP_EXISTING GH_PAT
export RED GREEN YELLOW BLUE NC
export SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Main function
main() {
    parse_args "$@"
    
    log_info "Starting SWE-PolyBench image upload script"
    log_info "Dataset: $DATASET_PATH"
    log_info "Version: $VERSION"
    log_info "Parallel jobs: $PARALLEL_JOBS"
    log_info "Dry run: $DRY_RUN"
    
    check_prerequisites
    
    log_info "Registry: $GHCR_REGISTRY"
    
    # Create temporary file for dataset processing
    local temp_dataset=$(mktemp)
    trap "rm -f $temp_dataset" EXIT
    
    log_info "Loading dataset..."
    
    # Get the directory where this script is located
    local script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    local dataset_script="${script_dir}/load_dataset.py"
    
    # Check if the dataset script exists
    if [[ ! -f "$dataset_script" ]]; then
        log_error "Dataset script not found: $dataset_script"
        exit 1
    fi
    
    # Use Python script to load and convert dataset to JSON lines
    local dataset_cmd="python3 $dataset_script $DATASET_PATH"
    if [[ -n "$OFFSET" ]]; then
        dataset_cmd="$dataset_cmd --offset $OFFSET"
        log_info "Skipping first $OFFSET instances"
    fi
    if [[ -n "$LIMIT" ]]; then
        dataset_cmd="$dataset_cmd --limit $LIMIT"
        log_info "Limiting to $LIMIT instances"
    fi
    
    $dataset_cmd > "$temp_dataset"
    
    if [[ $? -ne 0 ]]; then
        log_error "Failed to load dataset"
        exit 1
    fi
    
    local total_instances=$(wc -l < "$temp_dataset")
    log_info "Found $total_instances instances to process"
    
    if [[ $total_instances -eq 0 ]]; then
        log_warning "No instances found in dataset"
        exit 0
    fi
    
    # Process instances
    log_info "Starting image processing..."
    
    if [[ $PARALLEL_JOBS -eq 1 ]]; then
        # Sequential processing
        local processed=0
        local failed=0
        
        while IFS= read -r instance_data; do
            processed=$((processed + 1))
            local instance_id=$(echo "$instance_data" | jq -r '.instance_id')
            
            log_info "Processing $processed/$total_instances: $instance_id"
            
            if ! process_instance "$instance_data"; then
                failed=$((failed + 1))
                log_error "Failed to process $instance_id"
            fi
        done < "$temp_dataset"
        
        log_info "Processing complete. Processed: $processed, Failed: $failed"
    else
        # Parallel processing using GNU parallel if available
        if command -v parallel &> /dev/null; then
            log_info "Using GNU parallel for processing"
            
            # Create a wrapper script that reads instance data from a file
            local script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
            local wrapper_script=$(mktemp)
            cat > "$wrapper_script" << EOF
#!/bin/bash
# Import all the exported functions and variables
$(declare -f process_instance)
$(declare -f log_info)
$(declare -f log_success)
$(declare -f log_warning)
$(declare -f log_error)
$(declare -f image_exists_in_registry)
$(declare -f fix_pkg_config_dockerfile)
$(declare -f fix_debian_buster_dockerfile)
$(declare -f fix_poetry_version)
$(declare -f fix_huggingface_model_downloads)
$(declare -f fix_custom_reporter_path)
export GHCR_REGISTRY="$GHCR_REGISTRY"
export VERSION="$VERSION"
export DRY_RUN="$DRY_RUN"
export REPO_PATH="$REPO_PATH"
export SKIP_EXISTING="$SKIP_EXISTING"
export GH_PAT="$GH_PAT"
export RED="$RED"
export GREEN="$GREEN"
export YELLOW="$YELLOW"
export BLUE="$BLUE"
export NC="$NC"
export SCRIPT_DIR="$script_dir"

instance_file="\$1"
if [[ -f "\$instance_file" ]]; then
    instance_data=\$(cat "\$instance_file")
    process_instance "\$instance_data"
    rm -f "\$instance_file"
fi
EOF
            chmod +x "$wrapper_script"
            
            # Create individual files for each instance and process them
            local temp_dir=$(mktemp -d)
            local file_list=$(mktemp)
            
            local counter=0
            while IFS= read -r instance_data; do
                local instance_file="$temp_dir/instance_$counter.json"
                echo "$instance_data" > "$instance_file"
                echo "$instance_file" >> "$file_list"
                counter=$((counter + 1))
            done < "$temp_dataset"
            
            # Process files in parallel
            cat "$file_list" | parallel -j "$PARALLEL_JOBS" "$wrapper_script"
            
            # Cleanup
            rm -f "$wrapper_script" "$file_list"
            rm -rf "$temp_dir"
        else
            log_warning "GNU parallel not found, falling back to sequential processing"
            # Fall back to sequential processing
            local processed=0
            local failed=0
            
            while IFS= read -r instance_data; do
                processed=$((processed + 1))
                local instance_id=$(echo "$instance_data" | jq -r '.instance_id')
                
                log_info "Processing $processed/$total_instances: $instance_id"
                
                if ! process_instance "$instance_data"; then
                    failed=$((failed + 1))
                    log_error "Failed to process $instance_id"
                fi
            done < "$temp_dataset"
            
            log_info "Processing complete. Processed: $processed, Failed: $failed"
        fi
    fi
    
    if [[ "$DRY_RUN" == "true" ]]; then
        log_success "Dry run completed successfully!"
        log_info "To actually upload images, run without --dry-run flag"
    else
        log_success "Image upload completed successfully!"
        if [[ -f "package_settings_urls.txt" ]]; then
            local url_count=$(wc -l < package_settings_urls.txt)
            log_info "Generated package_settings_urls.txt with $url_count URLs for batch visibility changes"
            log_info "Open each URL and change visibility from 'Private' to 'Public'"
        fi
    fi
}

# Run main function with all arguments
main "$@"
