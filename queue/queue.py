# -*- coding: utf-8 -*-

from ..linkedlist import LinkedList


class EmptyError(Exception):
    pass


class Queue:

    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._item_linked_list = LinkedList()

    def __len__(self):
        return len(self._item_linked_list)

    def push(self, value):      # O(1)
        """队尾添加元素

        Arguments:
            value
        """
        return self._item_linked_list.append(value)

    def pop(self):
        """队列头部删除元素
        """
        if len(self) <= 0:
            raise EmptyError("empty queue")
        return self._item_linked_list.popleft()
