import time

import pytest
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
            self.dig_result += 20
            yield

dwarf1 = DwarfAgent()

def setup():
    global dwarf1

    dwarf1.start()
    manager.run()


def teardown():
    print("basic teardown into module")


def test_agent_task_yielding():
    global dwarf1
    time.sleep(4)

    assert dwarf1.dig_result >= 40
