from abc import ABC, abstractmethod
from typing import List

class File:
    def __init__(self, name: str, sz): 
        self.name: str = name; self.sz = sz
        self.e = []; self.is_directory = 0 if '.' in name else 1 
        self.extension = name.split('.')[1] if not self.is_directory else ""
    def __repr__(self): return '(' + self.name + '}'

class Filter(ABC):
    def __init__(self): pass
    @abstractmethod
    def apply(self, file: File): pass

class MinSizeFilter(Filter):
    def __init__(self, sz): self.sz = sz
    def apply(self, file: File): return file.sz > self.sz

class ExtensionFilter(Filter):
    def __init__(self, extension): self.extension = extension
    def apply(self, file: File): return file.extension == self.extension
        
class LinuxFind():
    def __init__(self): self.filters: List[Filter] = []
    def add_filter(self, filter): 
        if isinstance(filter, Filter): self.filters.append(filter)
    def OR(self, u):
        ans = []; q: List[File] = [u]
        while q:
            u = q.pop(0)
            if not u.is_directory:
                for filter in self.filters:
                    if filter.apply(u):
                        ans.append(u)
                        break
            else: q.extend(u.e)
        return ans
    def AND(self, u): 
        ans = []; q: List[File] = [u]
        while q:
            u = q.pop(0)
            if not u.is_directory:
                f = 1
                for filter in self.filters:
                    if not filter.apply(u):
                        f = 0; break
                if f: ans.append(u)
            else: q.extend(u.e)
        return ans

f1 = File("root_300", 300); f2 = File("fiction_100", 100); f3 = File("action_100", 100); f4 = File("comedy_100", 100)
f1.e = [f2, f3, f4]

f5 = File("StarTrek_4.txt", 4); f6 = File("StarWars_10.xml", 10); f7 = File("JusticeLeague_15.txt", 15); f8 = File("Spock_1.jpg", 1)
f2.e = [f5, f6, f7, f8]

f9 = File("IronMan_9.txt", 9); f10 = File("MissionImpossible_10.rar", 10); f11 = File("TheLordOfRings_3.zip", 3)
f3.e = [f9, f10, f11]

f12 = File("BigBangTheory_4.txt", 4); f13 = File("AmericanPie_6.mp3", 6)
f4.e = [f12, f13]

greater5_filter = MinSizeFilter(5); txt_filter = ExtensionFilter("txt")
my_linux_find = LinuxFind(); my_linux_find.add_filter(greater5_filter); my_linux_find.add_filter(txt_filter)

print(my_linux_find.OR(f1))
print(my_linux_find.AND(f1))
