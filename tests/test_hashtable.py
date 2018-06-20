from datastruct.hashtable import HashTable


def test_hashtable():
    h = HashTable()
    h.add('a', 0)
    h.add('b', 1)
    h.add('c', 2)

    assert len(h) == 3
    assert h.get('a') == 0
    assert h.get('b') == 1
    assert h.get("hehe") is None

    h.remove('a')
    assert h.get('a') is None
    assert sorted(list(h)) == ['b', 'c']

    # test rehash
    n = 50
    for i in range(n):
        h.add(i, i)

    for i in range(n):
        assert h.get(i) == i
