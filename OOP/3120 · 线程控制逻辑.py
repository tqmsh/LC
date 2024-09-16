import threading; import time

class Singleton(object):
    # __new__: 造地址时调用，比 __init__ 之前
    # cls: 指的是类本身，在这里它指的是 Singleton 类 
    # *args: 允许你向函数传递 任意数量的位置参数, f(1, 2, 3)
    # **kwargs: 任意数量的关键字参数， f(a = 1, b = 2, c = 3)
    def __new__(cls, *args, **kwargs):
        # 检查类是否已经有一个实例存在，如果不存在，就创建一个新的实例，并将其赋值
        if not hasattr(cls, '_instance'):  
            # super: 用 Singleton 的父类，做一个 cls, class, 即 self, 即 singleton; 就是用 object 造一个 singleton 类，这样的话，就算是有一个实例存在
            orig = super(Singleton, cls); cls._instance = orig.__new__(cls, *args, **kwargs)  
        return cls._instance  # 传回去

class Bus(Singleton):
    # 只让一个 Thread 用这个资源, Rlock allows thread to call same lock multiple time w/o blocking itself
    lock = threading.RLock()  

    def sendData(self, data):
        self.lock.acquire(); 
        time.sleep(1); 
        print(f"Sending Signal Data... {data}"); 
        # 🟥 修复了 release 没有调用的问题, 应该使用 self.lock.release() 来释放锁
        self.lock.release()  

class VisitEntity(threading.Thread): 
    # threading.thread: 代表一个单独的 thread, 每一个instance of 这个类自己在自己的 thread 里跑
    singleton = None; name = ""  
    def getName(self): return self.name
    def setName(self, name): self.name = name
    def run(self):
        # run: 当thread.start()时被启动, 用一个类 send data
        self.singleton = Bus(); self.singleton.sendData(self.name)  

if __name__ == "__main__":
    t1 = VisitEntity(); t1.setName("Thread 1")  # 🟥 线程对象创建和名称设置均在一行内完成
    t2 = VisitEntity(); t2.setName("Thread 2")
    t3 = VisitEntity(); t3.setName("Thread 3")

    # 启动线程
    t1.start(); t2.start(); t3.start()

    # 等待所有线程执行完毕
    t1.join(); t2.join(); t3.join()

    print("All threads have finished execution.")
