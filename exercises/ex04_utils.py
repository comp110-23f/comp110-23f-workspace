"""EX04 is the basic ideas of lists and working with them."""
__author__ = "730402747"


def all(l_input: list[int], i_input: int) -> bool: 
    """Returns if an imputted value exists in the inputted list."""
    var: int = 0
    if len(l_input) == 0:
        return False
    while var < len(l_input):
        if l_input[var] == i_input:
            var += 1
        else:
            return False 
    return True


def max(l_input: list[int]) -> int:
    """Returns the max value of a list."""
    if len(l_input) == 0:
        raise ValueError("max() arg is an empty List")
    var: int = 0
    max_val: int = l_input[0]
    while var < len(l_input):
        if max_val < l_input[var]:
            max_val = l_input[var]
        var += 1
    return max_val


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """Returns if two imputted list are the same as one anothet at all points."""
    if len(list_one) == len(list_two):
        var: int = 0
        while var < len(list_one):
            if list_one[var] == list_two[var]:
                var += 1
            else:
                return False 
        return True
    else:
        return False