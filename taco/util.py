import heapq


# 1. Add new item
# 2. Append to it priority
# 3. Get it
class DisplacingQueue:
    def __init__(self):
        self.items = []
        self.head = None

    def get(self):
        if self.head is None:
            self.head = heapq.heappop(self.items)
            return self.head

        return self.head

    def push(self, item, priority):
        _item = (priority, item)

        if self.head is None:
            self.head = _item
        else:
            if priority < self.head[0]:
                heapq.heappush(self.items, self.head)
                self.head = _item
            else:
                heapq.heappush(self.items, _item)
                return self.head

        return _item

    def pop(self):
        if self.head is not None:
            self.head = None
            self.head = heapq.heappop(self.items)

    def change(self, value):
        item = self.get()

        if item is not None:
            self.head = None
            return self.push(value, item[1])

    def size(self):
        acc = len(self.items)

        if self.head is not None:
            acc += 1

        return acc