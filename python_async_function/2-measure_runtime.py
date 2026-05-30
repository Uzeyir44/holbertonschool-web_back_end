#!/usr/bin/env python3
"""
IMported time, asyncio libraries and wait_n function
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    This function calculates the total time spent to execute the
    coroutine function

    Args:
        n (int): the numbers of coroutines that will be started
        max_delay (int): the limit of possible delay

    Returns:
        float: the total time spent on execution
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elaps = time.perf_counter() - start
    return (elaps)
