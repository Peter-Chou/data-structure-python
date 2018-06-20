from ..set import SetADT


def test_SetADT():
    set_a = SetADT()
    set_a.add(1)
    set_a.add(2)
    set_a.add(3)
    set_a.add(4)

    set_b = SetADT()
    set_b.add(3)
    set_b.add(4)
    set_b.add(5)
    set_b.add(6)

    assert sorted(list(set_a & set_b)) == [3, 4]
    assert sorted(list(set_a | set_b)) == [1, 2, 3, 4, 5, 6]
    assert sorted(list(set_a - set_b)) == [1, 2]
    assert sorted(list(set_a ^ set_b)) == [1, 2, 5, 6]

    set_b.remove(3)
    assert sorted(list(set_a & set_b)) == [4]
    assert sorted(list(set_a | set_b)) == [1, 2, 3, 4, 5, 6]
    assert sorted(list(set_a - set_b)) == [1, 2, 3]
    assert sorted(list(set_a ^ set_b)) == [1, 2, 3, 5, 6]
