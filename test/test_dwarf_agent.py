import time

from taco.manager import manager
from taco.tasks import task
from taco.tasks import agent


@agent
class DwarfAgent:
    def __init__(self):
        self.dig_result = 0

    @task("dig_task")
    def dig(self):
        while self.dig_result <= 100:
            self.dig_result += 40
            yield
        yield


def test_agent_task_yielding():
    dwarf1 = DwarfAgent()
    dwarf1.start()
    manager.run()

    time.sleep(2)

    assert dwarf1.dig_result >= 20
