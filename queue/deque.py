# -*- coding: utf-8 -*-

from ..linkedlist import CircularDoubleLinkedList


class FullError(Exception):
    pass


class EmptyError(Exception):
    pass


class Deque(CircularDoubleLinkedList):

    def pop(self):
        """删除尾节点"""
        if len(self) == 0:
            raise EmptyError("empty")
        tailnode = self.tailnode()
        value = tailnode.value
        self.remove(tailnode)
        return value

    def popleft(self):
        """删除首节点"""
        if len(self) == 0:
            raise EmptyError("empty")
        headnode = self.headnode()
        value = headnode.value
        self.remove(headnode)
        return value
