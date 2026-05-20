#!/usr/bin/env python3
"""
This module contains to_kv function
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This function that returns the tuple with given variables

    Args:
        k (str): first argument
        v (int/float): second argument
    Return:
        (tuple[str, float]): the tuple with given arguments
    """
    return (k, float(v**2))
