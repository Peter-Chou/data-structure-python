# -*- coding: utf-8 -*-

import pytest
from ..queue.array_queue import ArrayQueue


def test_array_queue():
    size = 5
    q = ArrayQueue(size)
    for i in range(size):
        q.push(i)

    with pytest.raises(Exception) as excinfo:
        q.push(size)
    assert excinfo.typename == "FullError"
    assert excinfo.value.args[0] == "queue full"

    assert len(q) == 5

    assert q.pop() == 0
    assert q.pop() == 1

    q.push(5)

    assert len(q) == 4

    assert q.pop() == 2
    assert q.pop() == 3
    assert q.pop() == 4
    assert q.pop() == 5

    assert len(q) == 0
