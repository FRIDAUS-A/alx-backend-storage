#!/usr/bin/env python3
"""
    a Python script that provides some stats
    about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


client = MongoClient('mongodb://127.0.0.1:27017')
nginx_collection = client.logs.nginx

print(f"{nginx_collection.count_documents({})} logs")
print("Methods:")
print(f"\tmethod GET: {nginx_collection.count_documents({'method': 'GET'})}")
print(f"\tmethod GET: {nginx_collection.count_documents({'method': 'POST'})}")
print(f"\tmethod GET: {nginx_collection.count_documents({'method': 'PUT'})}")
print(f"\tmethod GET: {nginx_collection.count_documents({'method': 'PATCH'})}")
delete_count = nginx_collection.count_documents({'method': 'DELETE'})
print(f"\tmethod GET: {delete_count}")
status_count = nginx_collection.count_documents({'path': '/status'})
print(f"{status_count} status check")
