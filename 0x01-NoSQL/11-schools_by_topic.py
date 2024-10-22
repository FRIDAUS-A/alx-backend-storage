#!/usr/bin/env python3
"""
    a Python function that returns the list of
    school having a specific topic
"""
from pymongo import MongoClient
from typing import List


def schools_by_topic(mongo_collection: MongoClient, topic: str) -> List:
    schools_by_topic = []
    for school in mongo_collection.find():
        if school.get("topics") and topic in school.get("topics"):
            schools_by_topic.append(school)
    return schools_by_topic
