from taco.manager import manager
from taco.tasks import task
from taco.tasks import agent


@agent
class DwarfAgent:
    def __init__(self, dig_percent, dig_task):
        self.dig_percent = dig_percent
        self.dig_task = dig_task

    @task("dig_task")
    def dig(self):
        dig_result = 0

        while dig_result <= 100:
            print(f"dig {dig_result}%")
            dig_result += self.dig_percent
            yield 2

dwarf1 = DwarfAgent(10, 25)
dwarf1.start()

manager.run()