import time

from taco.manager import manager
from taco.tasks import task


@task()
def drink_big_bear():
    while True:
        print(f"drinking")
        yield "doing"


@task()
def dig():
    size = 0
    percent = 10

    while size < 100:
        print(f"digging on {size}%")
        size = size + percent
        yield "doing"

    print(f"digging")

    yield "doing"


drink_big_bear(agent="dwarf-1", priority=10)
#dig(agent="dwarf-1", priority=5)

manager.run()
