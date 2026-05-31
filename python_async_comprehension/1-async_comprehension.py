#!/usr/bin/env python3
"""
Imported asyncio module and async_generator
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    This function uses async comprehension
    technique to get random values

    Returns:
        _type_: _description_
    """
    result = [x async for x in async_generator()]
    return (result)
