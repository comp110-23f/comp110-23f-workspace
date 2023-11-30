"""Combining two lists into a dictionary!"""

__author__ = "730664874"


def zip(key_list: list[str], val_list: list[int]) -> dict[str, int]:
    """Builds a dictionary using the first list as keys and the second list as values."""
    built_dict: dict[str, int] = dict()
    if (len(key_list) != len(val_list)):
        return built_dict
    for index in range(len(key_list)):
        built_dict[key_list[index]] = val_list[index]
    return built_dict