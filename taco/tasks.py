from typing import Callable

import taco.manager
import inspect
from taco.manager import manager


def task(name, priority = 0):
    def decorator(generator_func):
        def task_wrapper(self, *args, **kwargs):
            agent_id = kwargs.pop('agent', self)
            task_priority = kwargs.pop('priority', priority)
            task_name = kwargs.pop('name', name)

            if type(task_priority) is str:
                task_priority = getattr(self, task_priority)
                if callable(task_priority):
                    task_priority = task_priority()

            #calls generator and returns iterator
            manager.add_task(agent_id, generator_func(self, *args, **kwargs), task_priority)
        return task_wrapper
    return decorator


def agent(agent_cls):
    def has_decorator(func, decorator_name):
        while hasattr(func, '__wrapped__'):
            # The decorator is the function we are currently inspecting

            if func.__name__ == decorator_name:
                return True

            func = func.__wrapped__

        return func.__name__ == decorator_name

    methods = []

    for name, method in inspect.getmembers(agent_cls, predicate=inspect.isfunction):
        if has_decorator(method, 'task_wrapper'):
            methods.append(method)

    def start(self):
        for method in methods:
            method(self)

    setattr(agent_cls, 'start', start)

    return agent_cls