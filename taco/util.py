import queue
import heapq
from collections import namedtuple

queue_node = namedtuple("Node", ["id", "item", "priority", "nextNode", "swapped"])


# 1. Add new task
# 2. Append to it priority
# 3. Get it
class DisplacingLinkedQueue:
    def __init__(self):
        self.head = None
        self.append_items = []

    def get(self):
        """returns current item task if it is not presented in queue returns none"""

        #append new add tasks if it is needed be added to queue
        for append_item in self.append_items:
            next_lookup_node = self.head
            prev_lookup_node = None

            if next_lookup_node is None:
                self.head = append_item
                continue

            while not next_lookup_node is None:
                if next_lookup_node.swapped:
                    next_next_lookup_node = next_lookup_node.nextNode

                    if not prev_lookup_node is None:
                        prev_lookup_node.nextNode = next_next_lookup_node


                if next_lookup_node.priority < append_item.priority:
                    append_item.nextNode = next_lookup_node

                    if prev_lookup_node is None:
                        self.head = append_item
                    else:
                        prev_lookup_node.nextNode = append_item
                    continue

                prev_lookup_node = next_lookup_node
                next_lookup_node = next_lookup_node.nextNode

            if next_lookup_node is None:
                prev_lookup_node.nextNode = append_item

        self.append_items.clear()

        if not self.head is None:
            return self.head.item, self.head.id

        return None

    def pop(self, item_id):
        next_node = self.head

        while not next_node is None:
            if next_node.id == item_id:
                next_node.swapped = True
                break

            next_node = next_node.nextNode

    def push(self, item_id, item, priority):
        item = queue_node(item_id, item, priority, None, False)
        self.append_items.append(item)

    def size(self):
        pass