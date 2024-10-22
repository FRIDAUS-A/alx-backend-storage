#!/usr/bin/env python3
"""
    a Python function that changes all topics of a
    school document based on the name
"""
from typing import List
from pymongo import MongoClient


def update_topics(mongo_collection: MongoClient,
                  name: str, topics: List[str]) -> None:
    """
        Args:
            mongo_collection: collection instance
            name: filter
            topics: add topics
        Return:
            returns None
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
