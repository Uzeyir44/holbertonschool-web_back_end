#!/usr/bin/env python3
"""
two modules , namely asyncio and random were imported
"""
import asyncio
import random

async def wait_random(max_delay: int =10) -> float:
    """
    This function stops execution for a certain period of time
    and then returns this value

    Args:
        max_delay (int, optional): The limit till which the function is
        temporarily terminated. Defaults to 10.

    Returns:
        float: the amount if time during which function was stopped 
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return (delay)
