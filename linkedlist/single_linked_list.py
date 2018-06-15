# -*- coding: utf-8 -*-
"""
this file is attmpt to complement the linked list
"""


class Node(object):
    """
    链表的基本元素
    """

    def __init__(self, value=None, next=None):
        """
        :param value: 值
        :param next: Node对象，用来链接下个节点
        """
        self.value = value
        self.next = next

    def __str__(self):
        """
        easy for debug
        """
        return "<Node: value: {}, next={}>".format(self.value, self.next)

    __repr__ = __str__


class LinkedList(object):
    """Single Linked List ADT
    """

    def __init__(self, maxsize=None):
        """
        maxsize : int or None, optional
             (the default is None, which has no limit)
        """
        self.maxsize = maxsize
        self.root = Node()
        self.tailnode = None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, value):      # O(1)
        """
        append a node at the end
        """
        if self.maxsize is not None and len(self) > self.length:
            raise Exception("LinkedList is full")
        node = Node(value)      # cosntruct node
        tailnode = self.tailnode
        if tailnode is None:    # if list is empty, link the node behand root
            self.root.next = node
        else:       # link node behind tailnode if list is not empty
            tailnode.next = node
        self.tailnode = node
        self.length += 1

    def appendleft(self, value):
        """append a node to the head

        Arguments:
            value
        """
        headnode = self.root.next
        node = Node(value)
        self.root.next = node
        node.next = headnode
        self.length += 1

    def insert(self, value, new_value):
        """insert new_value befor value node

        Arguments:
            value
            new_value
        """
        prevnode = self.root
        curnode = self.root.next
        node = Node(new_value)
        for curnode in self.iter_node():
            if curnode.value == value:
                prevnode.next = node
                node.next = curnode
                self.length += 1
                return 1    # insert sucess
            prevnode = curnode
        return -1   # insert failed not found value

    def iter_node(self):
        """iterate from head to tail
        """
        curnode = self.root.next
        while curnode is not self.tailnode:
            yield curnode
            curnode = curnode.next      # move to next node
        yield curnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def remove(self, value):    # O(n) needs iterate all nodes
        """delete a node contains value

        Arguments:
            value
        """
        prevnode = self.root
        curnode = self.root.next
        for curnode in self.iter_node():
            if curnode.value == value:
                prevnode.next = curnode.next
                if curnode is self.tailnode:
                    self.tailnode = prevnode
                del curnode
                self.length -= 1
                return 1    # remove sucessfully
            else:
                prevnode = curnode      # keep update prevnode
        return -1  # remove failed

    def find(self, value):
        """find the node

        Arguments:
            value
        """
        index = 0
        for node in self.iter_node():
            if node.value == value:
                return value
            index += 1
        return -1       # not found

    def popleft(self):
        """delete the first node
        """
        if self.root.next is None:
            raise Exception("pop from empty Linkedlist is not allowed")
        headnode = self.root.next
        self.root.next = headnode.next
        self.length -= 1
        value = headnode.value
        del headnode
        return value

    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next = None
        self.length = 0
