#!/usr/bin/env python3
"""
Imported asyncio, random, and typing libraries
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    This function gathers the results of all coroutines
    and returns a sorted list of these results

    Args:
        n (int): the numbers of coroutines that will be started
        max_delay (int): the limit of possible delay

    Returns:
        List[float]: a list of all delays
    """
    ls = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    result = []
    for i in ls:
        result.append(await i)
    for i in range(n):
        for j in range(n - i - 1):
            if result[j] > result[j+1]:
                result[j], result[j+1] = result[j+1], result[j]
    return (result)
