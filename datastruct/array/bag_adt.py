# -*- coding: utf-8 -*-
"""
create a bag object
"""


class Bag(object):
    def __init__(self, maxsize=10):
        """ initial """
        self.maxsize = maxsize
        self._item = list()

    def add(self, item):
        if len(self._item) > self.maxsize:
            raise Exception("Bag is Full")
        self._item.append(item)

    def remove(self, item):
        self._item.remove(item)

    def __len__(self):
        return len(self._item)

    def __iter__(self):
        for item in self._item:
            yield item
