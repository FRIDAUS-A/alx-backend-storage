#!/usr/bin/env python3
"""
    a Python function that inserts a new document
    in a collection based on kwargs
"""
from pymongo import MongoClient
from typing import Dict


def insert_school(mongo_collection: MongoClient, **kwargs: Dict) -> str:
    """
        Args:
            mongo_cllection: collection instance
            kwargs: key value pair to pass
        Returns: the id of the new document
    """
    doc = mongo_collection.insert_one(kwargs)
    return str(doc.inserted_id)
