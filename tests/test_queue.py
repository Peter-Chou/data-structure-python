import pytest
from ..queue.queue import Queue


def test_queue():
    q = Queue()
    q.push(0)
    q.push(1)
    q.push(2)

    assert len(q) == 3

    assert q.pop() == 0
    assert q.pop() == 1
    assert q.pop() == 2

    with pytest.raises(Exception) as excinfo:
        q.pop()
    assert excinfo.typename == "EmptyError"
    assert excinfo.value.args[0] == "empty queue"
