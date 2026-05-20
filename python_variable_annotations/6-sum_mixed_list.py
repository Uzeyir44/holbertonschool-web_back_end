#!/usr/bin/env python3
"""
This module contains sum_mixed_list function
"""
from typing import *


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    This function that returns the sum of floats

    Args:
        mxd_lst (List[Union[int, float]]): list with floats and ints

    Return:
        (float): the sum of the list elements
    """
    return (sum(mxd_lst))
