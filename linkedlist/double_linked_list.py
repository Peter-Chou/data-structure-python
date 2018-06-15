# -*- coding: utf-8 -*-


class Node(object):

    def __init__(self, value=None, prev=None, next=None):
        self.value, self.prev, self.next = value, prev, next


class CircularDoubleLinkedList:
    """double linked list ADT
    """

    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        node = Node()
        node.prev, node.next = node, node
        self.root = node
        self.length = 0

    def __len__(self):
        return self.length

    def headnode(self):
        return self.root.next

    def tailnode(self):
        return self.root.prev

    def append(self, value):     # O(1)
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception("LinkedList is full")
        node = Node(value)
        tailnode = self.tailnode() or self.root

        tailnode.next = node
        node.prev = tailnode
        node.next = self.root
        self.root.prev = node
        self.length += 1

    def appendleft(self, value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception("LinkedList is full")
        node = Node(value)
        if self.root.next is self.root:     # empty
            node.next = self.root
            node.prev = self.root
            self.root.next = node
            self.root.prev = node
        else:
            headnode = self.headnode()
            node.next = headnode
            headnode.prev = node
            node.prev = self.root
            self.root.next = node
        self.length += 1

    def remove(self, node):     # O(1) delete node
        """remove
        :param node
        """
        if node is self.root:   # can't delete root node
            return
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1
        return node

    def iter_node(self):
        if self.root.next is self.root:
            return
        curnode = self.root.next
        while curnode.next is not self.root:
            yield curnode
            curnode = curnode.next
        yield curnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node_reverse(self):
        if self.root.prev is self.root:
            return
        curnode = self.root.prev
        while curnode.prev is not self.root:
            yield curnode
            curnode = curnode.prev
        yield curnode
