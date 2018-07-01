from datastruct.queue import PriorityQueue


def test_priority_queue():
    size = 5
    pq = PriorityQueue(size)
    pq.push(5, "purple")
    pq.push(0, "white")
    pq.push(3, "orange")
    pq.push(1, "black")

    res = []
    while not pq.is_empty():
        res.append(pq.pop())
    assert res == ["purple", "orange", "black", "white"]
