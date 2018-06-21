from datastruct.algorithm import binary_search


def test_binary_search():
    a = list(range(10))

    assert binary_search(a, 1) == 1
    assert binary_search(a, -1) == -1

    assert binary_search(None, 1) == -1

    assert binary_search(a, 0) == 0

    for i in range(10):
        assert binary_search(a, i) == i
