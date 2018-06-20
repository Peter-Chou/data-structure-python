# -*- coding: utf-8 -*-

from ..hashtable import HashTable


class SetADT(HashTable):

    def add(self, key):
        return super(SetADT, self).add(key, True)

    def remove(self, key):
        return super(SetADT, self).remove(key)

    def __and__(self, other_set):
        new_set = SetADT()
        for element_a in self:
            if element_a in other_set:
                new_set.add(element_a)
        return new_set

    def __sub__(self, other_set):
        new_set = SetADT()
        for element_a in self:
            if element_a not in other_set:
                new_set.add(element_a)
        return new_set

    def __or__(self, other_set):
        new_set = SetADT()
        for element_a in self:
            new_set.add(element_a)
        for element_b in other_set:
            new_set.add(element_b)
        return new_set

    def __xor__(self, other_set):
        return (self | other_set) - (self & other_set)
