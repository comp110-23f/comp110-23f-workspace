"""Summing the elements of a list using different loops!"""

__author__ = "730664874"


def w_sum(vals: list[float]) -> float:
    """Sums elements in val with a while loop!"""
    total: float = 0.0
    index: int = 0
    while (index < len(vals)):
        total += vals[index]
        index += 1
    return total


def f_sum(vals: list[float]) -> float:
    """Sums elements in val with a for-in loop!"""
    total: float = 0.0
    for val in vals:
        total += val
    return total


def f_range_sum(vals: list[float]) -> float:
    """Sums elements in val with a for-in-range loop!"""
    total: float = 0.0
    for index in range(len(vals)):
        total += vals[index]
    return total