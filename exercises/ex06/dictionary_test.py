"""Dictionary Tests!"""

__author__ = "730664874"

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_invert_use_standard_input() -> None:
    """Tests whether invert properly functions for an standard input of a dict[str, str] with keys and values being string."""
    dict1: dict[str, str] = {"Abid": "COMP 110", "Bob": "MATH 233", "Carl": "GEOG 121"}
    assert invert(dict1) == {"COMP 110": "Abid", "MATH 233": "Bob", "GEOG 121": "Carl"}


def test_invert_use_num_str_input() -> None:
    """Tests whether invert properly functions for an input of a dict[str, str] where the value is a numeric string."""
    dict1: dict[str, str] = {"Abid": "1", "Bob": "2", "Carl": "3"}
    assert invert(dict1) == {"1": "Abid", "2": "Bob", "3": "Carl"}


def test_invert_edge_empty_input() -> None:
    """Tests whether invert properly functions for an input of an empty dict."""
    dict1: dict[str, str] = dict()
    assert invert(dict1) == dict()


def test_favorite_color_use_standard_input() -> None:
    """Tests whether favorite_color works properly with mixed color values."""
    dict1: dict[str, str] = {"Abid": "Blue", "Bob": "Red", "Carl": "Blue"}
    assert favorite_color(dict1) == "Blue"


def test_favorite_color_use_same_input() -> None:
    """Tests whether favorite_color works properly with same color values."""
    dict1: dict[str, str] = {"Abid": "Blue", "Bob": "Blue", "Carl": "Blue"}
    assert favorite_color(dict1) == "Blue"


def test_favorite_color_edge_empty_input() -> None:
    """Tests whether favorite_color works properly with same color values."""
    dict1: dict[str, str] = dict()
    assert favorite_color(dict1) == ""


def test_count_use_standard_input() -> None:
    """Tests whether count works properly with mixed string values."""
    list1: list[str] = ["Bob", "Abid", "Bob"]
    assert count(list1) == {"Bob": 2, "Abid": 1}


def test_count_use_same_input() -> None:
    """Tests whether count works properly with same string values."""
    list1: list[str] = ["Bob", "Bob", "Bob"]
    assert count(list1) == {"Bob": 3}


def test_count_edge_empty_input() -> None:
    """Tests whether favorite_color works properly with same color values."""
    list1: list[str] = []
    assert count(list1) == dict()


def test_alphabetizer_use_standard_input() -> None:
    """Tests whether alphabetizer works properly with mixed string values."""
    list1: list[str] = ["Bob", "Abid", "Alice"]
    assert alphabetizer(list1) == {"b": ["Bob"], "a": ["Abid", "Alice"]}


def test_alphabetizer_use_same_input() -> None:
    """Tests whether alphabetizer works properly with same string values."""
    list1: list[str] = ["Alan", "Abid", "Alice"]
    assert alphabetizer(list1) == {"a": ["Alan", "Abid", "Alice"]}


def test_alphabetizer_edge_empty_input() -> None:
    """Tests whether alphabetizer works properly with same string values."""
    list1: list[str] = []
    assert alphabetizer(list1) == dict()


def test_update_attendance_use_day_in_attendance() -> None:
    """Tests whether update_attendance works where day of week is in the attendance dict."""
    dict1: dict[str, list[str]] = {"Monday": ["Alice"], "Tuesday": ["Bob", "Abid", "Alice"], "Wednesday": ["Bob", "Alice"]}
    day_of_week: str = "Monday"
    student_name: str = "Abid"
    assert update_attendance(dict1, day_of_week, student_name) == {"Monday": ["Alice", "Abid"], "Tuesday": ["Bob", "Abid", "Alice"], "Wednesday": ["Bob", "Alice"]}


def test_update_attendance_use_day_not_in_attendance() -> None:
    """Tests whether update_attendance works where day of week is not in the attendance dict."""
    dict1: dict[str, list[str]] = {"Monday": ["Alice"], "Tuesday": ["Bob", "Abid", "Alice"], "Wednesday": ["Bob", "Alice"]}
    day_of_week: str = "Friday"
    student_name: str = "Abid"
    assert update_attendance(dict1, day_of_week, student_name) == {"Monday": ["Alice"], "Tuesday": ["Bob", "Abid", "Alice"], "Wednesday": ["Bob", "Alice"], "Friday": ["Abid"]}


def test_update_attendance_edge_diff_student_name_case() -> None:
    """Tests whether update_attendance works where day of week is not in the attendance dict."""
    dict1: dict[str, list[str]] = {"Monday": ["Alice"], "Tuesday": ["Bob", "Abid", "Alice"], "Wednesday": ["Bob", "Alice"]}
    day_of_week: str = "Tuesday"
    student_name: str = "abid"
    assert update_attendance(dict1, day_of_week, student_name) == {"Monday": ["Alice"], "Tuesday": ["Bob", "Abid", "Alice", "abid"], "Wednesday": ["Bob", "Alice"]}