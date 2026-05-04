# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: CC-BY-NC-4.0
import functools
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional, Set, Union

from tree_sitter import Language, Parser, Tree

TREE_SITTER_LIBRARY_PATH = str(Path(__file__).parent / "languages.so")
try:
    from tree_sitter_languages import get_language
except ImportError:
    get_language = functools.partial(Language, TREE_SITTER_LIBRARY_PATH)

TREE_SITTER_FUNC_CLASS_TYPES = [
    "pair",
    "function_definition",
    "class_definition",
    "function_declaration",
    "method_declaration",
    "method_definition",
    "class_declaration",
    "constructor_declaration",
]

TREE_SITTER_TOP_LEVEL_NODE_TYPES = ["module", "program"]

TREE_SITTER_NAME_IDENTIFIER = [
    "identifier",
    "property_identifier",
    "type_identifier",
    "computed_property_name",
]


@dataclass
class LanguageTypeConfig:
    # The node types that represent important structural code elements
    types_to_retain: Set[str]
    # The node types that we want to retain only if defined at the top level of the syntax tree
    types_to_retain_if_top_level: Set[str]
    # The types of nodes that represent the names of objects in the class, function, and variable
    # types. If a node of one of these types exists as a child of one of the above types, we will
    # use the identifier node's text value as the name of the parent
    identifier_types: Set[str]
    # The node types to retain but should not result in an increment to the current effective level
    # For some node types, we don't want to increment the level as we dive into its children. This
    # enables us to handle cases such as namespaces in C#, where we want to include the namespace
    # in the XML tree, but do not want to prevent it from allowing us to include top-level-only
    # elements that are defined within.
    types_to_retain_without_level_increment: Set[str] = field(default_factory=set)
    # Effective top-level - used to determine retention of 'types_to_retain_if_top_level' nodes
    effective_top_level: int = 1

    # On creation, dynamically create a set of all allowed types
    def __post_init__(self):
        self.node_types = (
            self.types_to_retain
            | self.types_to_retain_if_top_level
            | self.types_to_retain_without_level_increment
        )


@dataclass
class LanguageConfig:
    # File extensions that are associated with a language
    extensions: Set[str]
    # Tree-Sitter language object
    tree_sitter_language_obj: Language
    # Language type configurations
    types: Optional[LanguageTypeConfig] = None


# Define supported tree-sitter languages
CODE_LANGUAGE_CONFIGS = {
    "java": LanguageConfig(
        extensions={".java"},
        tree_sitter_language_obj=get_language("java"),
        types=LanguageTypeConfig(
            types_to_retain={
                "class_declaration",
                "enum_declaration",
                "record_declaration",
                "annotation_type_declaration",
                "interface_declaration",
                "method_declaration",
                "constructor_declaration",
            },
            types_to_retain_if_top_level={"variable_declarator"},
            identifier_types={"identifier"},
            effective_top_level=2,
        ),
    ),
    "javascript": LanguageConfig(
        extensions={".js", ".jsx", ".cjs"},
        tree_sitter_language_obj=get_language("javascript"),
        types=LanguageTypeConfig(
            types_to_retain={"class_declaration", "function_declaration", "method_definition"},
            types_to_retain_if_top_level={"variable_declarator"},
            identifier_types={"identifier", "property_identifier", "type_identifier"},
        ),
    ),
    "python": LanguageConfig(
        extensions={".py", ".py-tpl", ".pyi"},
        tree_sitter_language_obj=get_language("python"),
        types=LanguageTypeConfig(
            types_to_retain={"class_definition", "with_statement", "function_definition"},
            types_to_retain_if_top_level={"assignment"},
            identifier_types={"identifier"},
        ),
    ),
    "typescript": LanguageConfig(
        extensions={".ts"},
        tree_sitter_language_obj=get_language("typescript"),
        types=LanguageTypeConfig(
            types_to_retain={
                "class_declaration",
                "type_alias_declaration",
                "enum_declaration",
                "interface_declaration",
                "function_declaration",
                "method_definition",
            },
            types_to_retain_if_top_level={"variable_declarator"},
            identifier_types={"identifier", "property_identifier", "type_identifier"},
        ),
    ),
}
EXTENSION_LANGUAGE_MAP = {
    ext: language_name
    for language_name, config in CODE_LANGUAGE_CONFIGS.items()
    for ext in config.extensions
}

parser = Parser()


def get_code_cst(content: str, file_path: Union[Path, str]) -> Tree:
    """Parse code and return tree-sitter concrete syntax tree.

    Args:
        content: The code content.
        file_path: The path to the code file, used to determine the code language.

    Returns:
        The concrete syntax tree or None if the language is not supported.
    """
    extension = Path(file_path).suffix
    language_name = EXTENSION_LANGUAGE_MAP.get(extension)

    if not language_name:
        return None

    # Define tree-sitter parser
    parser.set_language(CODE_LANGUAGE_CONFIGS[language_name].tree_sitter_language_obj)

    # Parse code
    content_bytes = content.encode()
    cst = parser.parse(content_bytes)
    return cst
