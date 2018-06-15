# -*- coding: utf-8 -*-

from ..array import Bag


def test_bag():
    bag = Bag()

    bag.add(1)
    bag.add(2)
    bag.add(3)

    assert len(bag) == 3

    bag.remove(3)
    assert len(bag) == 2

    for i in bag:
        print(i)
