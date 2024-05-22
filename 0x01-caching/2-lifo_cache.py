#!/usr/bin/python3
"""
h
e
y
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    class LIFOCache that inherits from
    BaseCaching and is a caching system:
    """
    def __init__(self):
        """
        Initiliaze
        """
        super().__init__()
        self.__stack = []

    def put(self, key, item):
        """
        Must assign to the dictionary
        self.cache_data the item value for the key key
        """
        if not key or not item:
            return
        if key in self.__stack:
            self.__stack.remove(key)
        if len(self.__stack) == self.MAX_ITEMS:
            self.cache_data.pop(self.__stack[-1])
            print('DISCARD: {}'.format(self.__stack.pop()))
        self.__stack.append(key)
        self.cache_data.update({key: item})

    def get(self, key):
        """
        Must return the value in
        self.cache_data linked to key.
        """
        return self.cache_data.get(key)
