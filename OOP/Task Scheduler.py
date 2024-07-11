import time, threading
from datetime import datetime, timedelta
from heapq import heappush, heappop
class Task:
    def __init__(self, name, start_time, action):
        self.name = name
        self.start_time = start_time
        self.action = action # 这个任务所绑定的函数
    def execute(self):
        print(f"Executing task {self.name}")
        self.action() # 时间到后调用这个函数
    def __lt__(self, other):
        return self.start_time < other.start_time
class TaskScheduler:
    def __init__(self):
        self.tasks = []
        self.running = 0
    def insert(self, task):
        heappush(self.tasks, task) 
    def run(self):
        self.running = 1
        while self.running:
            cur_time = datetime.now() # 运行时间 
            # The heapq module maintains the heap property, which means the smallest element is always 
            # # at the root (index 0), but the rest of the elements may not be sorted.
            while self.tasks and cur_time >= self.tasks[0].start_time: # 答案枚举
                print(self.tasks[0].name)
                task = heappop(self.tasks)
                task.execute()
            time.sleep(1)
    def stop(self):
        self.running = 0
def test():
    print(f"ran at {datetime.now()}")
DS = TaskScheduler()
DS.insert(Task("Test3", datetime.now() + timedelta(seconds = 500000), test))
DS.insert(Task("Test2", datetime.now() + timedelta(seconds = 50000), test))
DS.insert(Task("Test", datetime.now() + timedelta(seconds = 5), test)) # 驱动后的的五秒后跑 
scheduler_thread = threading.Thread(target=DS.run) # 系统一跑 DS
scheduler_thread.start()  
time.sleep(20) # 母系统倒计时
DS.stop()
scheduler_thread.join()