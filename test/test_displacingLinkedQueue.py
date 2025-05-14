from taco.util import DisplacingQueue


def setup():
    pass

def test_queue_insert():
    dis_queue = DisplacingQueue()

    dis_queue.push("20", 20)
    dis_queue.push("10",  10)
    dis_queue.push("30",  30)

    item10 = dis_queue.get()[1]
    dis_queue.pop()
    item20 = dis_queue.get()[1]
    dis_queue.pop()

    assert item20 == '20'
    assert item10 == '10'