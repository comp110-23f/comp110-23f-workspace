"""EX07 shows how to test to ensure functions work in normal and edge cases."""
__author__ = "730402747"

from exercises.ex06.dictionary import invert, count, favorite_color, alphabetizer, update_attendance
import pytest


def test_invert_unique() -> None: 
    """Output for unique keys in invert should give an inverted dictionary."""
    dictt: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(dictt) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_empty() -> None:
    """Output in the event of empty input should be empty."""
    empty: dict(str, str) = {}
    assert invert(empty) == {}


def test_invert_matchingkeys() -> None:
    """If there are matching keys then a KeyError should be raised."""
    with pytest.raises(KeyError):
        my_dictionary = {'alyssa': 'byrnes', 'adam': 'byrnes'}
        invert(my_dictionary)


def test_unequal_amounts_favorite() -> None:
    """With a clear favorite, that color should be returned."""
    colors: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(colors) == 'blue'


def test_empty_favorites() -> None:
    """Output in the event of empty input should be empty."""
    empty: dict(str, str) = {}
    assert favorite_color(empty) == ''


def test_equal_amounts_favorites() -> None:
    """If there is a tie raise am error."""
    colors: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Ella": "purple", "Charlotte": "yellow"}
    assert favorite_color(colors) == 'purple'


def test_longlist_count() -> None:
    """The count function returns the count for long lists of items."""
    listt: list[str] = ["apple", "apple", "orange", "apple", "grape", "berry", "grape", "apple"]
    assert count(listt) == {'apple': 4, 'orange': 1, 'grape': 2, 'berry': 1}


def test_stortlist_count() -> None:
    """The count function returns the count for a short list of items."""
    listt: list[str] = ["apple", "orange", "apple"]
    assert count(listt) == {'apple': 2, 'orange': 1}


def test_empty_count() -> None:
    """Output in the event of empty input should be empty."""
    empty_list: list(str) = ()
    assert count(empty_list) == {}


def test_uppercase_alphabetizer() -> None:
    """Alphabetizer should be able to handel upper case words."""
    wordss: list[str] = ["Python", "sugar", "Turtle", "party", "table"]
    assert alphabetizer(wordss) == {'p': ['Python', 'party'], 's': ['sugar'], 't': ['Turtle', 'table']}


def test_empty_alphabetizer() -> None:
    """Output in the event of empty input should be empty."""
    empty_list: list(str) = ()
    assert alphabetizer(empty_list) == {}


def test_one_empty_alphabetizer() -> None:
    """When given a string that is not a word in a list alphabetizer should raise an error."""
    wordss: list[str] = ["cat", "apple", "boy", "angry", "bad", "car", ""]
    assert alphabetizer(wordss) == "Error: One item is empty"


def test_normalattendence() -> None:
    """Updating attendence by adding a child to a preexisting day."""
    attendance_log: dict[str] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    day: str = "Tuesday"
    student: str = "Vrinda"
    assert update_attendance(attendance_log, day, student) == {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa', 'Vrinda']}


def test_newday_updateattendence() -> None:
    """Adding a new day to attendence."""
    attendance_log: dict[str] = {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa', 'Vrinda']}
    day: str = "Wednesday"
    student: str = "Kaleb"
    assert update_attendance(attendance_log, day, student) == {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa', 'Vrinda'], 'Wednesday': ['Kaleb']}


def test_empty_updateattendance() -> None:
    """Output in the event of empty input should be empty."""
    empty_dict: dict[str, list[str]] = {}
    empty_str: str = ''
    assert update_attendance(empty_dict, empty_str, empty_str) == {'': ['']}