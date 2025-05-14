import uuid
import time
import threading
from taco.util import DisplacingQueue


DONE = "TASK_DONE"
PROCESS = "TASK_PROCESS"


class Manager:
    def __init__(self, tick_time):
        self.pre_tasks = []
        self.tasks = {}
        self.loop_thread = None

        def loop():
            while True:
                time.sleep(tick_time)
                for agent_id in list(self.tasks.keys()):
                    agent_tasks : DisplacingQueue = self.tasks[agent_id]

                    if agent_tasks.size() == 0:
                        del self.tasks[agent_id]
                        continue

                    agent_priority, agent_task = agent_tasks.get()
                    agent_task_result = next(agent_task, DONE)

                    if agent_task_result == DONE:
                        agent_tasks.pop()
                    elif agent_task_result is not None:
                        agent_tasks.change(agent_priority + agent_task_result)

        self.loop_thread = threading.Thread(target=loop, name=f"Thread-TaskManager")

    def run(self):
        self.loop_thread.start()

    def add_task(self, agent_id, agent_task, priority):
        if agent_id not in self.tasks:
            self.tasks[agent_id] = DisplacingQueue()

        tasks : DisplacingQueue = self.tasks[agent_id]
        tasks.push(agent_task, priority)

        return self


manager = Manager(1)