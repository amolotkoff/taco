from taco.manager import manager
from taco.tasks import task
from taco.tasks import agent

@agent
class DwarfAgent:
    def __init__(self, dig_percent):
        self.dig_percent = dig_percent

    @task(10)
    def dig(self):
        dig_result = 0

        while dig_result <= 100:
            print(f"dig {dig_result}%")
            dig_result += self.dig_percent
            yield

    @task(20)
    def drink(self):
        for i in range(0, 3):
            print(f"drink {i}")
            yield

dwarf1 = DwarfAgent(10)
dwarf1.start()

dwarf2 = DwarfAgent(20)
dwarf2.start()

manager.run()