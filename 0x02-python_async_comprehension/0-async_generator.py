#!/usr/bin/env python3
'''Task 0'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]
   '''Generates a sequemce of 10 nbrs'''
   for _ in range(10):
       await asyncio.sleep(1)
       yield random.random() * 10
