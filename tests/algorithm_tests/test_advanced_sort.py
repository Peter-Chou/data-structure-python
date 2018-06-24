from datastruct.algorithm import merge_sort


def test_merge_sort():
    import random
    seq = list(range(10))
    random.shuffle(seq)
    assert merge_sort(seq) == sorted(seq)
