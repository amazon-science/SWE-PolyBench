# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: CC-BY-NC-4.0
import re
from copy import deepcopy
from functools import cached_property
from pathlib import Path
from typing import List, Optional, Union, cast

# type: ignore
from xml.etree.ElementTree import Element

from tree_sitter import Node, Parser, Tree
from typing_extensions import Self

from .tree_sitter_utils import CODE_LANGUAGE_CONFIGS, EXTENSION_LANGUAGE_MAP

parser = Parser()


class CodeElement(Element):
    """A code XML element."""

    def __init__(
        self,
        tag: str,
        start: int,
        end: int,
        header_start: Optional[int] = None,
        header_end: Optional[int] = None,
        parent: Optional[Self] = None,
        cst_node: Optional[Node] = None,
        attrib={},
        **extra,
    ):
        """Initialize the CodeElement class.

        Args:
            tag: The tag name for the XML element.
            start: The starting line number for the code element.
            end: The ending line number for the code element.
            header_start: The starting line number for the element's "header". Typically, this is
                equal to `start`.
            header_end: The ending line number for the element's "header", typically the line
                containing the element's identifier.
            parent: The parent CodeElement object.
            cst_node: The tree_sitter node corresponding to this code element.
            attrib: The attributes for the XML element.
            **extra: Additional keyword arguments are added as XML attributes.
        """
        super().__init__(tag, attrib, **extra)
        self.attrib["lines"] = f"{start}-{end}"
        self.start = start
        self.end = end
        self.header_start = header_start or start
        self.header_end = header_end or start + 1
        self.parent = parent
        self.cst_node = cst_node
        self.level: int = parent.level + 1 if parent is not None else 0

        if self.parent is not None:
            self.parent.insert_in_order(self)

    def find_smallest_enclosing_node(self, start, end):
        smallest_node = self
        for child in self:
            if child.start <= start and child.end >= end:  # type: ignore
                smallest_node = child.find_smallest_enclosing_node(start, end)  # type: ignore
        return smallest_node

    def insert_in_order(self, item: Self):
        if item in self:
            return
        for child in list(self):
            if child.start >= item.start and child.end <= item.end:  # type: ignore
                self.remove(child)
        self.append(item)
        self[:] = sorted(self, key=lambda c: cast("CodeElement", c).start)

    def append(self, item: Element) -> None:
        """Append item to the list of children."""
        if not isinstance(item, CodeElement):
            raise TypeError("Can only append CodeElement instances")
        if item in self:
            return
        super().append(item)
        item.parent = self

    def copy(self):
        """Recursively copy element and children to a new object."""
        if self.parent is not None:
            raise ValueError("Cannot copy element with a non-None parent")
        return self.__copy__()

    def __copy__(self):
        # Create a new element with the same tag and attributes
        new_element = CodeElement(
            tag=self.tag,
            start=self.start,
            end=self.end,
            header_start=self.header_start,
            header_end=self.header_end,
            parent=None,
            cst_node=self.cst_node,
            attrib=self.attrib.copy(),
        )
        new_element.level = self.level

        # Copy children recursively
        for child in self:
            new_child = child.__copy__()
            new_child.parent = new_element  # type: ignore
            new_element.append(new_child)

        return new_element


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


def find_node_name(node, return_line_number=True):
    names = []
    max_identifier_line = node.start_point[0] + 1
    for child in node.children:
        if any(keyword in child.type.lower() for keyword in ["identifier", "title", "heading"]):
            max_identifier_line = max(child.end_point[0] + 1, max_identifier_line)
            names.append(child.text.decode("utf-8"))
    if not names:
        node_lines = node.text.decode("utf-8").splitlines()
        first_line = node_lines[0] if node_lines else ""
        # Use left side of assignment for approximate name
        name = first_line.split("=")[0].strip()
    else:
        name = ";".join(names)
    if return_line_number:
        return name, max_identifier_line
    else:
        return name


def cst_to_xml(cst_node, max_depth=None, _code_node=None):
    # Initialize containers if required
    if _code_node is None:
        start_line = cst_node.start_point[0]
        end_line = cst_node.end_point[0] + 1
        _code_node = CodeElement(
            tag=cst_node.type,
            start=start_line,
            end=end_line,
            cst_node=cst_node,
        )

    # Exit early if we exceed max depth
    if max_depth and _code_node.level >= max_depth:
        return _code_node

    # Traverse tree
    for child_cst_node in cst_node.children:
        # Get tag name and name attribute
        tag_name = re.sub(r"[^\w\s_-]", "", child_cst_node.type)
        node_name, identifer_end_line = find_node_name(child_cst_node, return_line_number=True)

        # Get start line and end line
        start_line = child_cst_node.start_point[0]
        end_line = child_cst_node.end_point[0] + 1

        # Don't add nodes that don't have a tag name or name attribute
        if not tag_name.strip() or not node_name or not any(char.isalpha() for char in tag_name):
            cst_to_xml(child_cst_node, max_depth, _code_node)
            continue

        # Add an XML node
        child_code_node = CodeElement(
            tag=tag_name,
            start=start_line,
            end=end_line,
            cst_node=child_cst_node,
            name=node_name,
            header_start=start_line,
            header_end=identifer_end_line,
            parent=_code_node,
        )
        _code_node.append(child_code_node)
        cst_to_xml(child_cst_node, max_depth, child_code_node)

    return _code_node


class CodeFile:
    """Container for code file contents and different simplified representations"""

    def __init__(
        self,
        file_path: Union[Path, str],
        content: Optional[str] = None,
    ):
        """Constructor for the CodeFile class."""
        self.file_path = Path(file_path).expanduser().resolve()
        self._content = content
        self._original_content: Optional[str] = None

    @cached_property
    def content(self) -> Optional[str]:
        """Cached file content property."""
        _content = None
        if self._content is not None:
            _content = self._content
        else:
            with self.file_path.open("r") as f:
                try:
                    _content = f.read()
                except UnicodeDecodeError:
                    _content = None
        if self._original_content is None:
            self._original_content = deepcopy(_content)
        return _content

    def _get_check_content(self):
        if self.content is None:
            raise IndexError(f"No readable content in {self.file_path} without readable")
        return self.content

    @property
    def content_lines(self) -> List[str]:
        """Cached file content lines property."""
        content = self._get_check_content()
        lines = content.split("\n")
        return lines

    @cached_property
    def cst(self) -> Tree:
        """Cached CST representation of the file."""
        return get_code_cst(self._get_check_content(), self.file_path)

    @property
    def tree(self) -> CodeElement:
        return self.node

    @cached_property
    def node(self) -> CodeElement:
        """Cached XML tree representation of the file."""
        if self.cst is None:
            root_element = CodeElement(
                tag="content",
                start=0,
                end=len(self),
                name="content",
                header_start=0,
                header_end=1,
            )
            for line_no, line in enumerate(self.content_lines):
                child_element = CodeElement(
                    tag="line",
                    start=line_no,
                    end=line_no + 1,
                    name="line",
                    header_start=line_no,
                    header_end=line_no + 1,
                    parent=root_element,
                )
                root_element.append(child_element)
            return root_element
        return cst_to_xml(self.cst.root_node)

    def _traverse_cst(self):
        cursor = self.cst.walk()

        visited_children = False
        while True:
            if not visited_children:
                yield cursor.node
                if not cursor.goto_first_child():
                    visited_children = True
            elif cursor.goto_next_sibling():
                visited_children = False
            elif not cursor.goto_parent():
                break

    def __len__(self) -> int:
        return len(self.content_lines)
