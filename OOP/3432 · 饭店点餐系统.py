from typing import List
from collections import defaultdict

class BackSys: 
    def cook(self, dish): pass  # 烹饪菜肴

class MainFoodSys(BackSys): 
    def cook(self, dish): print(f"MAINFOOD: Cook {dish}")  # 主菜烹饪

class CoolDishSys(BackSys): 
    def cook(self, dish): print(f"COOLDISH: Cook {dish}")  # 冷菜烹饪

class HotDishSys(BackSys): 
    def cook(self, dish): print(f"HOTDISH: Cook {dish}")  # 热菜烹饪

class Cmd: 
    def __init__(self, sys: BackSys, dish): self.sys = sys; self.dish = dish  # 命令初始化
    def exec(self): pass  # 执行命令
    def notif(self): pass  # 通知系统

class FoodCmd(Cmd): 
    def exec(self): print("WAITER: Add dish")  # 增加菜品
    def notif(self): self.sys.cook(self.dish)  # 通知烹饪系统

class MainFoodCmd(FoodCmd): pass  # 主菜命令

class CoolDishCmd(FoodCmd): pass  # 冷菜命令

class HotDishCmd(FoodCmd): pass  # 热菜命令

class WaiterSys: 
    def __init__(self, menu: 'MenuAll', main_food_sys: BackSys, cool_dish_sys: BackSys, hot_dish_sys: BackSys): 
        self.cmds: List[Cmd] = []; self.menu = menu; self.main_food_sys = main_food_sys; self.cool_dish_sys = cool_dish_sys; self.hot_dish_sys = hot_dish_sys  # 服务员系统初始化 🟥 修复了 main_food_sys 参数丢失的问题
    def setOrder(self, dish: str): 
        if self.menu.isHot(dish): cmd = HotDishCmd(self.hot_dish_sys, dish); print("WAITER: Add hot dish")  # 添加热菜
        elif self.menu.isCool(dish): cmd = CoolDishCmd(self.cool_dish_sys, dish); print("WAITER: Add cool dish")  # 添加冷菜
        elif self.menu.isMain(dish): cmd = MainFoodCmd(self.main_food_sys, dish); print("WAITER: Add main dish")  # 添加主菜
        else: 
            print(f"Dish '{dish}' not found on the menu!"); return  # 菜品未找到
        self.cmds.append(cmd)  
    def notify(self): 
        print("WAITER: Notify")  # 通知系统
        for cmd in self.cmds: cmd.notif()  # 执行通知
        self.cmds.clear()   

class MenuAll: 
    def __init__(self): self.mp = defaultdict(list)  # 菜单初始化
    def loadMenu(self):  # 加载菜单
        self.mp["hot"] = ["Yu-Shiang Shredded Pork", "Sauteed Tofu, Home Style", "Sauteed Snow Peas"]  # 热菜
        self.mp["cool"] = ["Cucumber", "Preserved egg"]  # 冷菜
        self.mp["main"] = ["Rice", "Pie"]  # 主菜
    def isHot(self, dish): return dish in self.mp["hot"]  # 判断是否为热菜
    def isCool(self, dish): return dish in self.mp["cool"]  # 判断是否为冷菜
    def isMain(self, dish): return dish in self.mp["main"]  # 判断是否为主菜

# 测试用例
menu = MenuAll(); menu.loadMenu()  # 加载菜单
main_food_sys = MainFoodSys(); cool_dish_sys = CoolDishSys(); hot_dish_sys = HotDishSys()  # 系统初始化
waiter = WaiterSys(menu, main_food_sys, cool_dish_sys, hot_dish_sys)  # 服务员系统初始化

# 测试1：有效菜品
waiter.setOrder("Yu-Shiang Shredded Pork")  # 添加热菜
waiter.notify()  # 通知烹饪

# 测试2：无效菜品
waiter.setOrder("Pizza")  # 无效菜品测试
waiter.notify()  # 通知（应无输出）

# 测试3：冷菜
waiter.setOrder("Cucumber")  # 添加冷菜
waiter.notify()  # 通知烹饪

# 测试4：主菜
waiter.setOrder("Rice")  # 添加主菜
waiter.notify()  # 通知烹饪
