#!/usr/bin/env python3
"""
    A module to implememt a Cache class
"""
import redis
import uuid


class Cache:
    """
     A cache class
    """
    def __init__(self) -> None:
        """
            initialize the class Cache
        """
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: str | bytes | float | int) -> str:
        """
            store data in the random key generated
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
