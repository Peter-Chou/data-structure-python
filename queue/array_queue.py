# -*- coding: utf-8 -*-

from ..array.fixed_array import FixedArray


class FullError(Exception):
    pass


class ArrayQueue(object):
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.array = FixedArray(maxsize)
        self.head = 0
        self.tail = 0

    def push(self, value):
        if len(self) >= self.maxsize:
            raise FullError("queue full")
        self.array[self.head % self.maxsize] = value
        self.head += 1

    def pop(self):
        value = self.array[self.tail % self.maxsize]
        self.tail += 1
        return value

    def __len__(self):
        return self.head - self.tail
