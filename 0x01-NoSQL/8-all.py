#!/usr/bin/env python3
"""
    a Python function that lists all documents in a collection
"""
from pymongo import MongoClient
from typing import Dict, List


def list_all(mongo_collection: MongoClient) -> List[Dict]:
    """
        Args: mongo_collection
        Return: a dictionary
    """
    return mongo_collection.find()
