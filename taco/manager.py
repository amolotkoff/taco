import uuid
import time
import threading
from taco.util import TaskQueue


DONE = "TASK_DONE"
PROCESS = "TASK_PROCESS"


class Manager:
    def __init__(self, tick_time):
        self.tasks = {}
        self.loop_thread = None

        def loop():
            while True:
                time.sleep(tick_time)
                for agent_id in list(self.tasks.keys()):
                    agent_tasks = self.tasks[agent_id]

                    if agent_tasks.size() == 0:
                        del self.tasks[agent_id]
                        continue

                    agent_priority, agent_task_id, agent_task = agent_tasks.get()
                    agent_task_result = ""

                    try:
                        agent_task_result = next(agent_task)
                    except StopIteration:
                        agent_tasks.remove(agent_task_id)

                    if agent_task_result == DONE:
                        agent_tasks.remove(agent_task_id)

        self.loop_thread = threading.Thread(target=loop, name=f"Thread-TaskManager")

    def run(self):
        self.loop_thread.start()

    def add(self, agent_id, task_name, priority, agent_task):
        if agent_id not in self.tasks:
            self.tasks[agent_id] = TaskQueue()

        tasks = self.tasks[agent_id]
        tasks.put(priority, f"{agent_id}_{task_name}_{uuid.uuid4()}", agent_task)

        return self

manager = Manager(1)