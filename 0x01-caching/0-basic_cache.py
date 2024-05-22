#!/usr/bin/env python3
"""
h
e
y
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Create a class BasicCache
    that inherits from BaseCaching and is a caching system:
    """
    def __init__(self):
        """
        Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """
        If key or item is None,
        this method should not do anything.
        """
        if not key or not item:
            return
        self.cache_data.update({key: item})

    def get(self, key):
        """
         return the value in
         self.cache_data linked to key.
        """
        return self.cache_data.get(key)
