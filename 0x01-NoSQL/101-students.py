#!/usr/bin/env python3
"""
    a Python function that returns all students sorted by average score
"""
from pymongo import MongoClient
from typing import List


def top_students(mongo_collection: MongoClient) -> List:
    """
        Args:
            mongo_collection: instance of mongo class
        Return:
            return the sorted version based on average score
    """
    docs = mongo_collection.find()
    for school in docs:
        sum = 0
        count = 0
        for topic in school.get('topics'):
            sum += topic['score']
            count += 1
        average_score = sum / count
        mongo_collection.update_one({"_id": school.get("_id")},
                                    {"$set": {"averageScore": average_score}})
    return mongo_collection.find().sort({"averageScore": -1})
