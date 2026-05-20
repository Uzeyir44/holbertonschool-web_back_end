#!/usr/bin/env python3
"""
This module contains make_multiplier function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This function that returns a new function

    Args:
        multiplier (float): argument
    Return:
        (function): a new function
    """
    def func(el: float) -> float:
        """
        This function multiplies argument to multiplier

        Args:
            el (float): argument

        Return:
            (float): the multiplication of argument and multiplier
        """
        return (el * multiplier)

    return (func)
