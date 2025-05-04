import time

from taco.manager import manager
from taco.tasks import task


@task()
def drink_big_bear():
    print("drinking big bear")
    yield "doing"


@task()
def dig():
    size = 0
    percent = 10

    while size < 100:
        print(f"digging on {size}%")
        size = size + percent
        yield "doing"

    yield "TASK_DONE"


drink_big_bear(agent="dwarf-1", priority=10)
dig(agent="dwarf-1", priority=5)

manager.run()
