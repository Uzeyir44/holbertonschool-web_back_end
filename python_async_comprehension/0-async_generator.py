#!/usr/bin/env python3
"""
Imported ascyncio and random modules 
and also AsyncGenerator for annotation
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    This function is an asynchronous generator
    that yileds one number per second

    Yields:
        float: a random value
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield (random.uniform(0, 10))
