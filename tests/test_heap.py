from datastruct.heap import MaxHeap, MinHeap
import random


def test_maxheap():
    n = 5
    h = MaxHeap(n)
    for i in range(n):
        h.add(i)
    for i in reversed(range(n)):
        assert i == h.extract()


def test_minheap():
    n = 5
    h = MinHeap(n)
    for i in reversed(range(n)):
        h.add(i)
    for i in range(n):
        assert i == h.extract()
