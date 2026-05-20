#!/usr/bin/env python3
"""
This module contains make_multiplier function
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    This function returns the tuple with the elements of the list
    and their length

    Args:
        lst: the list of iterable elements

    Return:
        the elements of the list with their length
    """
    return [(i, len(i)) for i in lst]
