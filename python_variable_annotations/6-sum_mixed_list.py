#!/usr/bin/env python3
"""
This module contains sum_mixed_list function
"""
from typing import *


def sum_mixed_list(mxd_lst: List[float | int]) -> float:
    """
    This function that returns the sum of floats

    Args:
        mxd_lst (list[float | int]): list with floats and ints

    Return:
        (float): the sum of the list elements
    """
    return (sum(mxd_lst))
