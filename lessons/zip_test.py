"""Test my zip function!"""

__author__ = "730664874"

from lessons.zip import zip


def test_zip_edge_diff_length_inputs() -> None:
    """Checks the edge case of when there the list inputs' elements are of differing lengths."""
    key_list: list[str] = ["Abby", "Bob", "Carl"]
    val_list: list[int] = [1, 2]
    assert zip(key_list, val_list) == dict()


def test_zip_use_pos_ints() -> None:
    """Checks the use case where the val_list elements are ints greater than 0."""
    key_list: list[str] = ["Abby", "Bob", "Carl"]
    val_list: list[int] = [1, 2, 3]
    assert zip(key_list, val_list) == {"Abby": 1, "Bob": 2, "Carl": 3}


def test_zip_use_pos_and_neg_ints() -> None:
    """Checks the use case where the val_list elements can be any integer."""
    key_list: list[str] = ["Abby", "Bob", "Carl"]
    val_list: list[int] = [1, -2, 3]
    assert zip(key_list, val_list) == {"Abby": 1, "Bob": -2, "Carl": 3}