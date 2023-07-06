#!/usr/bin/env python3
'''Task 7'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Converts a key and its value to a tuple'''
    return (k, float(v**2))
