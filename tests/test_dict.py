from datastruct.dict import DictADT


def test_dict_adt():
    import random
    d = DictADT()

    d['a'] = 1
    assert d['a'] == 1
    d.remove('a')

    ll = list(range(30))
    random.shuffle(ll)
    for i in ll:
        d.add(i, i)

    for i in ll:
        assert d.get(i) == i

    assert sorted(list(d.keys())) == sorted(ll)
