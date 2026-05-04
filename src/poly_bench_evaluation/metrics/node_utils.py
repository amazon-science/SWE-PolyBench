# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: CC-BY-NC-4.0
from pathlib import Path
from typing import Optional, Union

from tree_sitter import Node, Tree

from .code_file import CodeFile
from .tree_sitter_utils import (
    TREE_SITTER_FUNC_CLASS_TYPES,
    TREE_SITTER_NAME_IDENTIFIER,
    TREE_SITTER_TOP_LEVEL_NODE_TYPES,
    get_code_cst,
)


def _get_node_identifier(node: Node) -> str:
    assert (
        node.type not in TREE_SITTER_TOP_LEVEL_NODE_TYPES
    ), "Node with identifier can't be a top-level node."
    func_or_class_name = [
        n.text.decode("utf-8") for n in node.children if n.type in TREE_SITTER_NAME_IDENTIFIER
    ]
    if len(func_or_class_name) >= 1:
        return "_".join(func_or_class_name)
    else:
        # For node.type == 'pair' it is not uncommon
        # to not find an identity
        if node.type == "pair":
            return []
        else:
            raise ValueError(f"Found no identifier for {node}")


def _find_inner_most_node(tree: Tree, line_number: int) -> Node:
    """Recursively find the inner most node in the tree that corresponds to the given line number.
    If the line corresponds to a function or class definition, return that node.
    Otherwise, return the root node of the tree which is of type `module`.

    Args:
        tree: Concrete syntax tree to search.
        line_number: Line number to find the corresponding node for.

    Returns:
        The inner most function, class, or module Node object containing the line number.
    """
    root_node = tree.root_node

    def traverse(node: Node) -> Union[Node, None]:
        if node.start_point[0] + 1 <= line_number <= node.end_point[0] + 1:
            matching_node = None
            if node.type in TREE_SITTER_FUNC_CLASS_TYPES:
                if node.type == "pair":
                    # If there is any function defined in this pair,
                    # we return the pair node which contains the name.
                    function_child = next(
                        (child for child in node.children if child.type == "function"), None
                    )
                    if function_child:
                        matching_node = function_child
                    else:
                        matching_node = None
                else:
                    matching_node = node

            for child in reversed(node.children):
                result = traverse(child)
                if result:
                    matching_node = result

            return matching_node
        return None

    result = traverse(root_node)
    return result if result else root_node


def get_node_by_line_number(file_path: Union[Path, str], line_number: int) -> Optional[Node]:
    """
    Find and return the node in the tree that corresponds to the given line number.

    Args:
        tree: The Tree object to search.
        line_number: The line number to find the corresponding node for.

    Returns:
        The Node object corresponding to the given line number. If the line number is outside of the file,
        return None.
    """
    if line_number <= 0:
        raise ValueError("Line number must be a positive integer.")

    cf = CodeFile(file_path=file_path)

    if line_number > cf.node.end - 1:
        return None

    tree = get_code_cst(content=str(cf.content), file_path=cf.file_path)

    return _find_inner_most_node(tree, line_number) if tree else None


def _find_identifiable_parent(node: Node) -> Node:
    if node.parent is not None:
        if node.parent.type in TREE_SITTER_TOP_LEVEL_NODE_TYPES + TREE_SITTER_FUNC_CLASS_TYPES:
            return node.parent
        else:
            return _find_identifiable_parent(node.parent)
    else:
        return node


def get_parent_id(node: Node) -> Optional[str]:
    if node.parent is not None:
        parent_node = _find_identifiable_parent(node)
        if parent_node.type in TREE_SITTER_TOP_LEVEL_NODE_TYPES:
            return parent_node.type
        else:
            return f"{parent_node.type}:{_get_node_identifier(parent_node)}"
    else:
        return None
