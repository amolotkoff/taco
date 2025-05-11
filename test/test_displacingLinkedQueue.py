from taco.util import DisplacingLinkedQueue


dis_queue = DisplacingLinkedQueue

def setup():
    pass

def test_queue_insert():
    dis_queue = DisplacingLinkedQueue()

    dis_queue.push("10", 10, 10)
    dis_queue.push("20", 20, 20)

    item20 = dis_queue.get()
    item10 = dis_queue.get()

    assert item20 == 20
    assert item10 == 10