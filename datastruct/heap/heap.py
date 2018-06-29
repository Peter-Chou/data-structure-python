# -*- coding: utf-8 -*-

from ..array import FixedArray


class MaxHeap(object):
    """
    完全二叉树，最大堆的非叶子节点的值都比孩子大，最小堆的非叶子结点的值都比孩子小
    Heap包含两个属性，order property 和 shape property(a complete binary tree)，在插入
    一个新节点的时候，始终要保持这两个属性
    插入操作：保持堆属性和完全二叉树属性, sift-up 操作维持堆属性
    extract操作：只获取根节点数据，并把树最底层最右节点copy到根节点后，sift-down操作维持堆属性
    用数组实现heap，从根节点开始，从上往下从左到右给每个节点编号，则根据完全二叉树的
    性质，给定一个节点i， 其父亲和孩子节点的编号分别是:
        parent = (i-1) // 2
        left = 2 * i + 1
        rgiht = 2 * i + 2
    使用数组实现堆一方面效率更高，节省树节点的内存占用，一方面还可以避免复杂的指针操作，减少
    调试难度。

    """

    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._elements = FixedArray(maxsize)
        self._count = 0

    def __len__(self):
        return self._count

    def add(self, value):
        if self._count >= self.maxsize:
            raise Exception("Full")
        self._elements[self._count] = value
        self._count += 1
        self._siftup(self._count-1)

    def _siftup(self, ndx):
        if ndx > 0:     # 只要不是根节点, 就判断是否需要往上交换
            parent = int((ndx-1)/2)
            if self._elements[ndx] > self._elements[parent]:
                self._elements[ndx], self._elements[parent] = \
                    self._elements[parent], self._elements[ndx]
                self._siftup(parent)

    def extract(self):
        if self._count <= 0:
            raise Exception("Empty")
        value = self._elements[0]
        self._count -= 1
        self._elements[0] = self._elements[self._count]  # 最右下节点放到root并siftdown
        self._siftdown(0)
        return value

    def _siftdown(self, ndx):
        left = 2 * ndx + 1
        right = 2 * ndx + 2
        largest = ndx
        if (left < self._count and
            self._elements[left] >= self._elements[largest] and
                self._elements[left] >= self._elements[right]):
            largest = left
        elif right < self._count and self._elements[right] >= self._elements[largest]:
            largest = right
        if largest != ndx:
            self._elements[ndx], self._elements[largest] = \
                self._elements[largest], self._elements[ndx]
            self._siftdown(largest)


class MinHeap(object):
    """最小堆，夫节点始终比孩子节点小
    """

    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._elements = FixedArray(maxsize)
        self._count = 0

    def __len__(self):
        return self._count

    def add(self, value):
        if self._count >= self.maxsize:
            raise Exception("Full")
        self._elements[self._count] = value
        self._count += 1
        self._siftup(self._count-1)

    def _siftup(self, ndx):
        if ndx > 0:     # 只要不是根节点, 就判断是否需要往上交换
            parent = int((ndx-1)/2)
            if self._elements[ndx] < self._elements[parent]:
                self._elements[ndx], self._elements[parent] = \
                    self._elements[parent], self._elements[ndx]
                self._siftup(parent)

    def extract(self):
        if self._count <= 0:
            raise Exception("Empty")
        value = self._elements[0]
        self._count -= 1
        self._elements[0] = self._elements[self._count]  # 最右下节点放到root并siftdown
        self._siftdown(0)
        return value

    def _siftdown(self, ndx):
        left = 2 * ndx + 1
        right = 2 * ndx + 2
        smallest = ndx
        if (left < self._count and
            self._elements[left] <= self._elements[smallest] and
                self._elements[left] <= self._elements[right]):
            smallest = left
        elif right < self._count and self._elements[right] <= self._elements[smallest]:
            smallest = right
        if smallest != ndx:
            self._elements[ndx], self._elements[smallest] = \
                self._elements[smallest], self._elements[ndx]
            self._siftdown(smallest)
