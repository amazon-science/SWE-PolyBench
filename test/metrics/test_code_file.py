import pytest

from poly_bench_evaluation.metrics.code_file import CodeElement, CodeFile


@pytest.fixture
def sample_content():
    return "def hello():\n    print('Hello, World!')\n\nprint('End of file')"


@pytest.fixture
def code_file(tmp_path, sample_content):
    file_path = tmp_path / "test_file.py"
    file_path.write_text(sample_content)
    return CodeFile(file_path)


class TestCodeFile:

    def test_initialization(self, tmp_path):
        file_path = tmp_path / "test.py"
        code_file = CodeFile(file_path)

        assert code_file.file_path == file_path

    def test_content_property(self, code_file, sample_content):
        assert code_file.content == sample_content

    def test_content_lines_property(self, code_file):
        assert code_file.content_lines == [
            "def hello():",
            "    print('Hello, World!')",
            "",
            "print('End of file')",
        ]

    def test_cst_property(self, code_file):
        cst = code_file.cst
        assert cst is not None
        assert hasattr(cst, "root_node")

    def test_node_property(self, code_file):
        node = code_file.node
        assert isinstance(node, CodeElement)
        assert node.tag == "module"

    def test_tree_property(self, code_file):
        tree = code_file.tree
        assert isinstance(tree, CodeElement)
        assert tree.tag == "module"

    def test_len(self, code_file):
        assert len(code_file) == 4
