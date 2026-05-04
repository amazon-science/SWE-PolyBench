from collections import defaultdict
from pathlib import Path

import pytest
from sklearn.metrics import precision_score, recall_score

from poly_bench_evaluation.metrics.patch_metrics import (
    file_precision,
    file_recall,
    file_retrieval_metrics,
)
from poly_bench_evaluation.metrics.patch_utils import Patch

sample_reference_patch = """
diff --git a/src/main.py b/src/main.py
index 1234567..8901234 100644
--- a/src/main.py
+++ b/src/main.py
@@ -10,7 +10,7 @@ def main():
     print("Hello, World!")
-    print("This is a test program.")
+    print("This is an updated test program.")
-    result = calculate_sum(5, 10)
+    result = calculate_sum(10, 20)
     print(f"The sum is: {result}")

diff --git a/README.md b/README.md
index abcdef0..1234567 100644
--- a/README.md
+++ b/README.md
@@ -1,5 +1,7 @@
 # My Project

-This is a simple test project.
+This is a simple test project with some updates.
"""

sample_predicted_patch_same_path = """
diff --git a/src/main.py b/src/main.py
index 1234567..8901234 100644
--- a/src/main.py
+++ b/src/main.py
@@ -10,7 +10,7 @@ def main():
     print("Hello, World!")
-    print("This is a test program.")
+    print("This is an updated test program.")
-    result = calculate_sum(5, 10)
+    result = calculate_sum(10, 20)
     print(f"The sum is: {result}")

diff --git a/src/utils.py b/src/utils.py
index abcdef0..1234567 100644
--- a/src/utils.py
+++ b/src/utils.py
@@ -1,3 +1,5 @@
 def helper_function():
     pass
+def new_helper_function():
+    a = test
+    return True
"""


sample_predicted_patch_diff_path = """
diff --git a/src/bar/main.py b/src/bar/main.py
index 1234567..8901234 100644
--- a/src/bar/main.py
+++ b/src/bar/main.py
@@ -10,7 +10,7 @@ def main():
     print("Hello, World!")
-    print("This is a test program.")
+    print("This is an updated test program.")

-    result = calculate_sum(5, 10)
+    result = calculate_sum(10, 20)
     print(f"The sum is: {result}")

diff --git a/src/utils.py b/src/utils.py
index abcdef0..1234567 100644
--- a/src/utils.py
+++ b/src/utils.py
@@ -1,3 +1,5 @@
 def helper_function():
     pass
+def new_helper_function():
+    return True
"""

sample_predicted_patch_low_file_precision_high_recall = """
diff --git a/src/bar/main.py b/src/bar/main.py
index 1234567..8901234 100644
--- a/src/bar/main.py
+++ b/src/bar/main.py
@@ -10,7 +10,7 @@ def main():
     print("Hello, World!")
-    print("This is a test program.")
+    print("This is an updated test program.")

-    result = calculate_sum(5, 10)
+    result = calculate_sum(10, 20)
     print(f"The sum is: {result}")

diff --git a/README.md b/README.md
index abcdef0..1234567 100644
--- a/README.md
+++ b/README.md
@@ -1,5 +1,7 @@
 # My Project

-This is a simple test project.
+This is a simple test project with some updates.

diff --git a/foo.md b/foo.md
index abcdef0..1234567 100644
--- a/foo.md
+++ b/foo.md
@@ -1,5 +1,7 @@
 # My Project

-This is a simple test project.
+This is a simple test project with some updates.

diff --git a/bar.md b/bar.md
index abcdef0..1234567 100644
--- a/bar.md
+++ b/bar.md
@@ -1,5 +1,7 @@
 # My Project

-This is a simple test project.
+This is a simple test project with some updates.
"""

sample_reference_diff_node_metrics_python = """diff --git a/test/metrics/example_files/example_file.py b/test/metrics/example_files/example_file.py
index 127bf42..5672a5d 100644
--- a/test/metrics/example_files/example_file.py
+++ b/test/metrics/example_files/example_file.py
@@ -1,5 +1,4 @@
 # flake8: noqa
-line_2 = "line_2"
 
 
 def func_1():
@@ -11,7 +10,6 @@ def func_1():
         line_2 = "f2_line_2"
 
         def func_3():
-            line_1 = "f3_line_1"
             line_2 = "f3_line_2"
 
     class class_1:
@@ -26,6 +24,7 @@ def func_1():
 class class_2:
     line_1 = "c2_line_1"
     line_2 = "c2_line_2"
+    line_3 = "c2_line_3"
 
     def func_5(self):
         line_1 = "c2_f5_line_1"
"""

sample_predicted_diff_node_metrics_python = """diff --git a/test/metrics/example_files/example_file.py b/test/metrics/example_files/example_file.py
index 127bf42..702dc60 100644
--- a/test/metrics/example_files/example_file.py
+++ b/test/metrics/example_files/example_file.py
@@ -11,7 +11,6 @@ def func_1():
         line_2 = "f2_line_2"
 
         def func_3():
-            line_1 = "f3_line_1"
             line_2 = "f3_line_2"
 
     class class_1:
@@ -30,3 +30,9 @@ class class_2:
     def func_5(self):
         line_1 = "c2_f5_line_1"
         line_2 = "c2_f5_line_2"
+
+def func_6():
+    pass
+
+def func_7():
+    pass"""


@pytest.mark.parametrize(
    "reference_patch, predicted_patch, expected_recall, expected_recall_basename",
    [
        (sample_reference_patch, sample_reference_patch, 1.0, 1.0),
        (sample_reference_patch, sample_predicted_patch_same_path, 0.5, 0.5),
        (sample_reference_patch, sample_predicted_patch_diff_path, 0.0, 0.5),
        (sample_reference_patch, sample_predicted_patch_low_file_precision_high_recall, 0.5, 1.0),
    ],
)
def test_file_recall(reference_patch, predicted_patch, expected_recall, expected_recall_basename):
    """
    Test the file_recall function with sample patches.

    This test verifies that the file_recall function correctly calculates
    the recall of retrieved files in the predicted patch over the ground
    truth files in the reference patch.

    Args:
        reference_patch: A reference patch.
        predicted_patch: A predicted patch.
        expected_recall: Expected recall based on the full path.
        expected_recall_basename: Expected recall based on the basename.
    """
    reference_patch_ = Patch(reference_patch)
    predicted_patch_ = Patch(predicted_patch)

    recall = file_recall(reference_patch_, predicted_patch_)
    assert recall == expected_recall, f"Expected recall of {expected_recall}, but got {recall}"

    recall_basename = file_recall(reference_patch_, predicted_patch_, to_basename=True)
    assert (
        recall_basename == expected_recall_basename
    ), f"Expected recall of {expected_recall_basename} with to_basename=True, but got {recall_basename}"

    retrieval_metrics = file_retrieval_metrics(reference_patch_, predicted_patch_)
    assert retrieval_metrics.recall == expected_recall

    retrieval_metrics = file_retrieval_metrics(reference_patch_, predicted_patch_, to_basename=True)
    assert retrieval_metrics.recall == expected_recall_basename


@pytest.mark.parametrize(
    "reference_patch, predicted_patch, expected_precision, expected_precision_basename",
    [
        (sample_reference_patch, sample_reference_patch, 1.0, 1.0),
        (sample_reference_patch, sample_predicted_patch_same_path, 0.5, 0.5),
        (sample_reference_patch, sample_predicted_patch_diff_path, 0.0, 0.5),
        (sample_reference_patch, sample_predicted_patch_low_file_precision_high_recall, 0.25, 0.5),
    ],
)
def test_file_precision(
    reference_patch, predicted_patch, expected_precision, expected_precision_basename
):
    """
    Test the file_precision function with sample patches.

    This test verifies that the file_precision function correctly calculates
    the precision of retrieved files in the predicted patch over the ground
    truth files in the reference patch.

    Args:
        reference_patch: A reference patch.
        predicted_patch: A predicted patch.
        expected_precision: Expected precision based on the full path.
        expected_precision_basename: Expected precision based on the basename.
    """

    reference_patch_ = Patch(reference_patch)
    predicted_patch_ = Patch(predicted_patch)

    precision = file_precision(reference_patch_, predicted_patch_)
    assert (
        precision == expected_precision
    ), f"Expected precision of {expected_precision}, but got {precision}"

    precision_basename = file_precision(reference_patch_, predicted_patch_, to_basename=True)
    assert (
        precision_basename == expected_precision_basename
    ), f"Expected precision of {expected_precision_basename} with to_basename=True, but got {precision_basename}"

    retrieval_metrics = file_retrieval_metrics(reference_patch_, predicted_patch_)
    assert retrieval_metrics.precision == expected_precision


@pytest.mark.parametrize(
    "reference_patch, predicted_patch, expected_recall, expected_precision",
    [
        (
            sample_reference_diff_node_metrics_python,
            sample_reference_diff_node_metrics_python,
            1.0,
            1.0,
        ),
        (
            sample_reference_diff_node_metrics_python,
            sample_predicted_diff_node_metrics_python,
            0.5,
            1 / 3,
        ),
    ],
)
def test_node_recall(reference_patch, predicted_patch, expected_recall, expected_precision):
    """
    Test the node_recall function with sample patches.

    This test verifies that the node_recall function correctly calculates
    the recall of retrieved node changes in the predicted patch over the ground
    truth modified nodes in the reference patch.

    Args:
        reference_patch: A reference patch.
        predicted_patch: A predicted patch.
        expected_recall: Expected recall based on the nodes.
    """

    def _merge_nodes(pre_change_nodes, post_change_nodes):
        merged = defaultdict(set)
        for d in [pre_change_nodes, post_change_nodes]:
            for k, v in d.items():
                merged[k].update(v)
        return merged

    # First get reference nodes
    reference_patch_ = Patch(reference_patch)
    old_modified_lines, new_modified_lines, _ = reference_patch_._get_modified_lines_by_status(
        as_dict=True
    )

    root_path = str(Path(__file__).parent.parent.parent)

    changed_old_nodes = reference_patch_._get_nodes(old_modified_lines, repo_root_path=root_path)
    # Pretend to apply patch as done in actual metric calculation (patch_utils.get_modified_nodes)
    # by overwriting that path to the new file.
    new_modified_lines = {
        "test/metrics/example_files/applied/example_file.py": new_modified_lines[
            "test/metrics/example_files/example_file.py"
        ]
    }
    changed_new_nodes = reference_patch_._get_nodes(new_modified_lines, repo_root_path=root_path)

    reference_nodes = _merge_nodes(changed_old_nodes, changed_new_nodes)
    reference_nodes = set(
        [
            f"{file}->{cst_path}"
            for file, cst_path_set in reference_nodes.items()
            for cst_path in cst_path_set
        ]
    )

    # Then get predicted nodes
    predicted_patch_ = Patch(predicted_patch)
    old_modified_lines, new_modified_lines, _ = predicted_patch_._get_modified_lines_by_status(
        as_dict=True
    )

    changed_old_nodes = predicted_patch_._get_nodes(old_modified_lines, repo_root_path=root_path)
    # Pretend to apply patch as done in actual metric calculation (patch_utils.get_modified_nodes)
    # by overwriting that path to the new file.
    new_modified_lines = {
        "test/metrics/example_files/applied/example_file.py": new_modified_lines[
            "test/metrics/example_files/example_file.py"
        ]
    }
    changed_new_nodes = predicted_patch_._get_nodes(new_modified_lines, repo_root_path=root_path)

    predicted_nodes = _merge_nodes(changed_old_nodes, changed_new_nodes)
    predicted_nodes = set(
        [
            f"{file}->{cst_path}"
            for file, cst_path_set in predicted_nodes.items()
            for cst_path in cst_path_set
        ]
    )

    # Create binary labels for each node in the union of reference and predicted nodes
    all_nodes = list(reference_nodes.union(predicted_nodes))
    y_true = [int(file in reference_nodes) for file in all_nodes]
    y_pred = [int(file in predicted_nodes) for file in all_nodes]

    recall = recall_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)

    assert (
        recall == expected_recall
    ), f"Expected recall of {expected_recall}, but got recall {recall}"

    assert (
        precision == expected_precision
    ), f"Expected recall of {expected_recall}, but got precision {precision}"
