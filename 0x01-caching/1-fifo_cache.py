#!/usr/bin/python3
"""
h
e
y
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    lass FIFOCache that inherits
    from BaseCaching and is a caching system:
    """
    def __init__(self):
        """
        Initiliaze
        """
        super().__init__()
        self.__queue = []

    def put(self, key, item):
        """
        If key or item is None,
        this method should not do anything.
        """
        if not key or not item:
            return
        elif key not in self.__queue:
            self.__queue.append(key)
        if len(self.__queue) > self.MAX_ITEMS:
            self.cache_data.pop(self.__queue[0])
            print('DISCARD: {}'.format(self.__queue.pop(0)))
        self.cache_data.update({key: item})

    def get(self, key):
        """
        Must return the value in
        self.cache_data linked to key.
        """
        return self.cache_data.get(key)
