# SWE-PolyBench Leaderboard

This directory contains the web-based leaderboard for SWE-PolyBench, a multi-language evaluation benchmark for coding agents.

## Overview

SWE-PolyBench provides a comprehensive framework for evaluating the performance of AI coding assistants across multiple programming languages. This leaderboard visualizes the results of these evaluations, allowing for easy comparison between different models and approaches.

## Directory Structure

- `polybench.html` - The main leaderboard webpage (generated from template)
- `css/` - Stylesheets for the leaderboard interface
- `img/` - Images and visual assets
- `template/` - HTML templates and data used for generating the leaderboard
  - `generate_polybench.py` - Python script to generate the leaderboard HTML
  - `polybench_data.json` - JSON data file containing benchmark results
  - `template_polybench.html` - Jinja2 template for the leaderboard

## Usage

### Viewing the Leaderboard
To view the leaderboard locally:
1. Open `polybench.html` in a web browser
2. Navigate through the different metrics and language tabs to compare model performance

### Generating the Leaderboard
To update the leaderboard with new data:

1. Make sure you have Python and Jinja2 installed:
   ```
   pip install jinja2
   ```

2. Update the `template/polybench_data.json` file with new benchmark results
   - The JSON file contains structured data about model performance across languages and metrics
   - Each model entry includes scores for different languages (Java, Python, JavaScript, TypeScript)
   - Various metrics are tracked (resolved rate, precision, recall, etc.)

3. Run the generation script from the template directory:
   ```
   cd template
   python generate_polybench.py
   ```

4. The script will generate a new `polybench.html` file in the leaderboard root directory


## Contributing

To add new benchmark results to the leaderboard:
1. Follow the evaluation protocol in the main SWE-PolyBench repository
2. Format your results according to the structure in `polybench_data.json`
3. Update the JSON data file with your new results
4. Regenerate the leaderboard using the steps above
5. Test the leaderboard locally before submitting changes

## Related Resources

- [SWE-PolyBench Main Repository](https://github.com/your-org/SWE-PolyBench)
- [Evaluation Methodology](https://github.com/your-org/SWE-PolyBench/docs/methodology.md)
- [Data Format Specification](https://github.com/your-org/SWE-PolyBench/docs/data-format.md)

## License

See the LICENSE file in the root directory for licensing information.
