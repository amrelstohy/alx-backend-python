#!/usr/bin/env python3
"""Complex types - list of floats"""


def sum_list(input_list: list[float]) -> float:
    """type-annotated function sum_list"""
    sum: float = 0.0
    for val in input_list:
        sum = sum + val
    return sum
