# 观察者模式又叫做发布订阅模式，观察者模式的定义如下：在对象之间定义一个一对多的关联，
# 当一个对象状态改变的时候，所有下游关联的对象都会自动收到通知并做出相应改变。
# 下游对象就是观察者，而上游对象就是被观察者。

from collections import defaultdict
from typing import List, Optional
from datetime import datetime

class Task:
    def __init__(self, content: str = None, date: datetime = None): 
        self.content = content
        self.date = date
    def __str__(self) -> str:
        return f"Task: {self.content}, DDL {self.date.strftime('%Y-%m-%d')}"

# Observer
class Observer:
    def update(self, tasks: List[Task] = []): pass
    def del_task(self, index: int): pass
    def list_tasks(self): pass

class TaskExecutioner(Observer):
    def __init__(self, name: str): 
        self.name = name
        self.tasks: List[Task] = [Task()]
    
    def update(self, tasks: List[Task]):
        for task in tasks:
            print(f"{self.name} received {task}")
            self.tasks.append(task)
    
    def del_task(self, index: int):
        if 1 <= index < len(self.tasks):
            task = self.tasks.pop(index)
            print(f"{self.name} finished {task}")
        else:
            print("Invalid Index")
    
    def list_tasks(self):
        if len(self.tasks) == 1:
            print(f"{self.name} has no tasks")
        else:
            print(f"{self.name}'s tasks:")
            for i in range(1, len(self.tasks)): print(f"{i}: {self.tasks[i]}")
                

class Subject:
    def add_observer(self, key: str, observer: Observer): pass
    def remove_observer(self, key: str): pass
    def notify_observer(self, tasks: List[Task]): pass

class TaskPublisher(Subject):
    def __init__(self): 
        self.observers: defaultdict[str, Observer] = defaultdict(Observer)
    
    def add_observer(self, key: str, observer: Observer): 
        self.observers[key] = observer
    
    def remove_observer(self, key: str): 
        del self.observers[key]
    
    def notify_observer(self, tasks: List[Task]):
        for observer in self.observers.values():
            observer.update(tasks)
    
class Solution:
    def __init__(self, publisher: TaskPublisher): 
        self.publisher = publisher
    
    @staticmethod
    def create_executioner(name: str) -> TaskExecutioner: 
        return TaskExecutioner(name)
    
    def bind_executioners(self, executioners: dict[str, TaskExecutioner]):
        for key, executioner in executioners.items():
            self.publisher.add_observer(key, executioner)
    
    def post_tasks(self, tasks: List[Task]): 
        self.publisher.notify_observer(tasks)

def test_solution():
    task_publisher = TaskPublisher()
    solution = Solution(task_publisher)

    tom = solution.create_executioner("Tom")
    jerry = solution.create_executioner("Jerry")

    solution.bind_executioners({'observer1': tom, 'observer2': jerry})

    task1 = Task("Print out materials for the meeting.", datetime(2022, 8, 31))
    task2 = Task("Hold a meeting.", datetime(2022, 8, 31))
    solution.post_tasks([task1])

    tom.list_tasks()
    tom.del_task(1)  
    tom.list_tasks()
    tom.del_task(99)
    solution.publisher.remove_observer('observer1')
    solution.post_tasks([task2])  
    tom.list_tasks()
    jerry.list_tasks()
    
test_solution()
