from ..hashtable import HashTable


def test_hashtable():
    h = HashTable()
    h.add('a', 0)
    h.add('b', 1)
    h.add('c', 2)

    assert len(h) == 3
    assert h.get('a') == 0
