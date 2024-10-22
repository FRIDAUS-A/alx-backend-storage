#!/usr/bin/env python3
"""
    a Python function that lists all documents in a collection
"""
from pymongo import MongoClient
from typing import Dict


def list_all(mongo_collection: MongoClient) -> Dict:
    return mongo_collection.find()
