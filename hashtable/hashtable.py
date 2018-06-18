# -*- coding: utf-8 -*-

from ..array import FixedArray


class Slot(object):
    """定义了hashtable的槽
    注意，一个槽有三种状态，看你能否想明白。相比链接法解决冲突，二次探查法删除一个 key 的操作稍微复杂。
    1.从未使用 HashMap.UNUSED。此槽没有被使用和冲突过，查找时只要找到 UNUSED 就不用再继续探查了
    2.使用过但是 remove 了，此时是 HashMap.EMPTY，该探查点后边的元素扔可能是有key
    3.槽正在使用 Slot 节点
    """

    def __init__(self, key, value):
        self.key, self.value = key, value


class HashTable(object):

    UNUSED = None   # 没被使用过
    EMPTY = Slot(None, None)    # 用过但是被删除了

    def __init__(self):
        self._table = FixedArray(8, init=HashTable.UNUSED)  # 保持2**i 次方
        self.length = 0

    @property
    def _load_factor(self):
        # 如果 load_factor 超过0.8 rehash
        return self.length / float(len(self._table))

    def __len__(self):
        return self.length  # hashtable已经使用的数量

    def _hash(self, key):
        return abs(hash(key)) % len(self._table)

    def _find_key(self, key):
        index = self._hash(key)
        _len = len(self._table)  # hashtable的capacity
        while self._table[index] is not HashTable.UNUSED:
            if self._table[index] is HashTable.EMPTY:   # 槽为空
                index = (index * 5 + 1) % _len
                continue
            elif self._table[index].key == key:  # 槽有值且为key
                return index
            else:               # 槽有值但不为key
                index = (index * 5 + 1) % _len
        return None

    def _slot_can_insert(self, index):
        return (self._table[index] is HashTable.EMPTY or
                self._table[index] is HashTable.UNUSED)

    def _find_slot_for_insert(self, key):
        index = self._hash(key)
        _len = len(self._table)
        while not self._slot_can_insert(index):
            index = (index * 5 + 1) % _len
        return index

    def __contains__(self, key):    # 重新定义 in operator
        index = self._find_key(key)
        return index is not None

    def add(self, key, value):
        if key in self:
            index = self._find_key(key)
            self._table[index] = value
            return False
        else:
            index = self._find_slot_for_insert(key)
            self._table[index] = Slot(key, value)
            self.length += 1
            if self._load_factor >= 0.8:
                self._rehash()
            return True

    def _rehash(self):
        old_table = self._table
        newsize = len(self._table) * 2
        self._table = FixedArray(newsize, HashTable.UNUSED)
        self.length = 0
        for slot in old_table:
            if slot is not HashTable.UNUSED and slot is not HashTable.EMPTY:
                index = self._find_slot_for_insert(slot.key)
                self._table[index] = slot
                self.length += 1

    def get(self, key, default=None):
        index = self._find_key(key)
        if index is None:
            return default
        else:
            return self._table[index].value

    def remove(self, key):
        index = self._find_key(key)
        if index is None:
            raise KeyError()
        value = self._table[index].value
        self.length -= 1
        self._table[index] = HashTable.EMPTY
        return value

    def __iter__(self):
        for slot in self._table:
            if slot not in (HashTable.UNUSED, HashTable.EMPTY):
                yield slot.key
