import queue
import heapq


class TaskQueue:
    def __init__(self):
        self.pq = []
        self.remove_tasks = set()
        self.add_tasks = []

    def get(self):
        if len(self.remove_tasks) > 0 or len(self.add_tasks) > 0:
            new_pq = []

            for (priority, task_id, task) in self.pq:
                if task_id not in self.remove_tasks:  # Only add items that are still in the dictionary
                    heapq.heappush(new_pq, (priority, task_id, task))

            for task in self.add_tasks:
                heapq.heappush(new_pq, task)

            self.remove_tasks.clear()
            self.add_tasks.clear()

            self.pq = new_pq  # Replace old queue with the new one

        return self.pq[0]

    def put(self, priority, task_id, task):
        heapq.heappush(self.add_tasks, (priority, task_id, task))

    def remove(self, task_id):
        self.remove_tasks.add(task_id)

    def size(self):
        return len(self.pq) + len(self.add_tasks) - len(self.remove_tasks)