class Coffee:
    def __init__(self, cost = 2): self.cost = cost
    def get_cost(self): return self.cost
    def get_ingredients(self): return "Plain Coffee"

class DarkRoast(Coffee):
    def __init__(self): super().__init__()
    def get_ingredients(self): return "DarkRoast"

class Expresso(Coffee):
    def __init__(self): super().__init__(3)
    def get_ingredients(self): return "Expresso"

# 装饰器模式（Decorator Pattern）允许向一个现有的对象添加新的功能，同时又不改变其结构。这种类型的设计模式属于结构型模式，它是作为现有的类的一个包装。
# 装饰器模式通过将对象包装在装饰器类中，以便动态地修改其行为。
# 这种模式创建了一个装饰类，用来包装原有的类，并在保持类方法签名完整性的前提下，提供了额外的功能。
# 我们通过下面的实例来演示装饰器模式的用法。其中，我们将把一个形状装饰上不同的颜色，同时又不改变形状类。

class Decorator(Coffee): 
    def __init__(self, coffee: Coffee):
        super().__init__(coffee.cost)
        self.coffee: Coffee = coffee # 在原 Coffee 类上搞事情

class WithMilk(Decorator):
    def __init__(self, coffee: Coffee): super().__init__(coffee); self.cost += 0.2
    def get_ingredients(self): return self.coffee.get_ingredients() + ", Milk"

class WithSugar(Decorator):
    def __init__(self, coffee: Coffee): super().__init__(coffee); self.cost += 0.5
    def get_ingredients(self): return self.coffee.get_ingredients() + ", Sugar"

class CoffeePack:
    def __init__(self, milk_cnt, sugar_cnt): self.milk_cnt = milk_cnt; self.sugar_cnt = sugar_cnt

class CoffeeMaker:
    def __init__(self, coffeePack: CoffeePack, Kind):
        self.coffee: Coffee = None
        if Kind == 'DarkRoast': self.coffee = DarkRoast()
        elif Kind == 'Expresso': self.coffee = Expresso()
        for _ in range(coffeePack.milk_cnt): self.coffee = WithMilk(self.coffee)
        for _ in range(coffeePack.sugar_cnt): self.coffee = WithSugar(self.coffee)

p1 = CoffeePack(2, 2)
d1 = CoffeeMaker(p1, "Expresso")
print(d1.coffee.get_ingredients())
print(d1.coffee.get_cost())