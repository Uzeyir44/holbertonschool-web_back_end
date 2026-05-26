#!/usr/bin/python3
"""
three modules , namely asyncio, time, and random were imported
"""
import asyncio
import time
import random

async def wait_random(max_delay=10):
    """
    This function stops execution for a certain period of time
    and then returns this value

    Args:
        max_delay (int, optional): The limit till which the function is
        temporarily terminated. Defaults to 10.

    Returns:
        float: the amount if time during which function was stopped 
    """
    start = time.perf_counter()
    await asyncio.sleep(random.uniform(0, max_delay))
    return (time.perf_counter() - start)
