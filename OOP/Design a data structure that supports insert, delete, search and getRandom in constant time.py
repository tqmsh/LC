from random import randint
class OOP: 
    def __init__(self): 
        self.a = [] # id -> v
        self.mp = {} # v -> id
    def insert(self, x):
        if x in self.mp: return
        self.a.append(x)
        self.mp[x] = len(self.a) - 1
    def remove(self, x):
        if x not in self.mp: return 
        x_id = self.mp[x]; lst = self.a[-1] # (1) 拿数据, 防 Edge Case，i.e. x_id == -1, 这样的话你一 pop, 两个一个没剩；mp 重布置的不知道是谁
        self.a[x_id] = lst # (2) 变动 a
        self.a.pop() 
        self.mp[lst] = x_id # (3) 变动 mp
        del self.mp[x] # 如果怕以前删删不完整（后面又被加回来了，因为是去重的，那么就最后删除
    def search(self, x): 
        return self.mp.get(x, -1)
    def getRandom(self):
        if not self.a: return None # 🟥 Edge Case   
        return self.a[randint(0, len(self.a) - 1)]
    def retrieve(self, index):
        if index < 0 or index >= len(self.a): return None  # or raise an exception
        return self.a[index]
    
ds = OOP()  
print(ds.getRandom())