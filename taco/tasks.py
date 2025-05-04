import taco.manager
import inspect
from taco.manager import manager


def task():
    def decorator(generator_func):
        def wrapper(*args, **kwargs):

            agent_id = kwargs.pop('agent', None)
            task_priority = kwargs.pop('priority', None)

            #calls generator and returns iterator
            manager.add(agent_id, generator_func.__name__, task_priority, generator_func(*args, **kwargs))
        return wrapper
    return decorator