#!/usr/bin/env python3
"""
This module contains sum_list function
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    This function that returns the sum of floats

    Args:
        input_list (list[float]): list with floats

    Return:
        (float): the sum of the list elements
    """
    return (sum(input_list))
