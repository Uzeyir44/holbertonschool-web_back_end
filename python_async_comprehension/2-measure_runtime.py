#!/usr/bin/env python3
"""
Imported asyncio and time modules and additionally
async_comprehension function
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    This function executes paralelly four
    coroutine functions

    Returns:
        float: the total time spent on the execution
    """
    start = time.perf_counter()
    ls = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*ls)
    return (time.perf_counter() - start)
