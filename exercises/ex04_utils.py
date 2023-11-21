"""EX04 - List Utility Functions!"""

__author__ = "730664874"


def all(int_list: list[int], integer: int) -> bool:
    """Returns if all the values in int_list match the value of integer."""
    if (len(int_list) == 0):
        return False
    index: int = 0
    while (index < len(int_list)):
        if (int_list[index] != integer):
            return False
        index += 1
    return True


def max(int_list: list[int]) -> int:
    """Returns the largest value in int_list."""
    if (len(int_list) == 0):
        raise ValueError("max() arg is an empty List")
    max_int: int
    index = 0
    while (index < len(int_list)):
        if (index == 0):
            max_int = int_list[index]
        elif (int_list[index] > max_int):
            max_int = int_list[index]
        index += 1
    return max_int


def is_equal(int_list1: list[int], int_list2: list[int]) -> bool:
    """Returns whether the elements in int_list1 are equal to and at the same indicies to int_list2."""
    if (len(int_list1) != len(int_list2)):
        return False
    index: int = 0
    while (index < len(int_list1)):
        if (int_list1[index] != int_list2[index]):
            return False
        index += 1
    return True

print(max([]))