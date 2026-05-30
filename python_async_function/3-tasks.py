#!/usr/bin/env python3
"""
Imported wait_random function
"""
wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    This function wrpas coroutines into tasks

    Args:
        max_delay (int): the argumet that will be passes into wait_random function

    Returns:
        asyncio.Task: the cocroutine wrapped into task
    """
    task = asyncio.create_task(wait_random(max_delay))
    return (task)
