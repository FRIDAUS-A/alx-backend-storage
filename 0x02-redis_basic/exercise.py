#!/usr/bin/env python3
"""
    A module to implememt a Cache class
"""
import redis
import uuid
from typing import Union


class Cache:
    """
     A cache class
    """
    def __init__(self):
        """
            initialize the class Cache
        """
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, int, bytes, float]
              ) -> str:
        """
            store data in the random key generated
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
