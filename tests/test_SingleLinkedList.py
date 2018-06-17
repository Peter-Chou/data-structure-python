from ..linkedlist import LinkedList


def test_linked_list():
    ll = LinkedList()

    ll.append(0)
    ll.append(1)
    ll.append(2)
    ll.append(3)

    assert len(ll) == 4
    assert ll.find(2) == 2
    assert ll.find(-1) == -1

    assert ll.remove(0) == 1
    assert ll.remove(10) == -1
    assert ll.remove(2) == 1
    assert len(ll) == 2
    assert list(ll) == [1, 3]
    assert ll.find(0) == -1

    ll.appendleft(0)
    assert list(ll) == [0, 1, 3]
    assert len(ll) == 3

    headvalue = ll.popleft()
    assert headvalue == 0
    assert len(ll) == 2
    assert list(ll) == [1, 3]

    ll.clear()
    assert len(ll) == 0
    assert 0


def test_linked_list_remove():
    ll = LinkedList()
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.remove(7)
    print(list(ll))


def test_linked_list_insert():
    ll = LinkedList()
    ll.append(3)
    ll.append(4)
    ll.append(5)
    result = ll.insert(4, 10)
    assert result == 1
    assert len(ll) == 4
    assert list(ll) == [3, 10, 4, 5]

    result = ll.insert(100, 1000)
    assert result == -1
