# -*- coding: utf-8 -*-
from ..stack import Stack


def test_stack():
    s = Stack()
    s.push(0)
    s.push(1)
    s.push(2)

    assert s.pop() == 2
    assert s.pop() == 1
    assert s.pop() == 0
