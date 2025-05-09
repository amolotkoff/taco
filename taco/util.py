import queue
import heapq
from collections import namedtuple


class TaskQueue:
    def __init__(self):
        self.task_node = namedtuple("TaskNode", ["priority", "id", "task", "nextNode"])
        self.head = None
        self.remove_tasks = set()
        self.add_tasks = []

    def get(self):
        """returns current item task if it is not presented in queue returns none"""

        #append new add tasks if it is needed be added to queue
        for add_task in self.add_tasks:
            append_task_priority = add_task[0]
            append_task_id = add_task[1]
            append_task = add_task[2]

            if self.head is None:
                self.head = self.task_node(append_task_priority, append_task_id, append_task, None)
            else:
                if self.head.priority < append_task_priority:
                    task = self.head
                    self.head = self.task_node(append_task_priority, append_task_id, append_task, task)
                else:
                    task = self.head
                    prev_task = None

                    while task.priority > append_task_priority:
                        if task.nextNode is None:
                            break

                        prev_task = task
                        task = task.nextNode
                            
                    task.

        return not self.head is None if self.head.task else None

    def put(self, priority, task_id, task):
        pass

    def put(self, priority):
        pass

    def remove(self, task_id):
        pass

    def remove(self):
        pass


    def size(self):
        pass