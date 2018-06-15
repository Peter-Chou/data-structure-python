# -*- coding: utf-8 -*-

from ..linkedlist.double_linked_list import CircularDoubleLinkedList


class FullError(Exception):
    pass


class Deque(object):
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.dll = CircularDoubleLinkedList(maxsize)
        self.length = 0

    def append(self, value):
        self.dll.append(value)

    def appendleft(self, value):
        self.dll.appendleft(value)

    def pop(self):
        tail = self.dll.tailnode()
        node = self.dll.remove(tail)
        return node.value

    def popleft(self):
        head = self.dll.headnode()
        node = self.dll.remove(head)
        return node.value

    def __len__(self):
        return len(self.dll)

    def __iter__(self):
        for node in self.dll.iter_node():
            yield node.value
