class Person:
    def __init__(self, name: str, mediator: 'Mediator'): self.name = name; self.mediator: 'Mediator' = mediator
    def contact(self, msg: str): 
        print(f'{self.name} sends msg: {msg}'); self.mediator.contact(msg, self)
    def receive_msg(self, msg: str): pass

class HouseOwner(Person):
    def receive_msg(self, msg: str): print(f'House owner {self.name} receives msg: {msg}')

class Tenant(Person):
    def receive_msg(self, msg: str): print(f'Tenant {self.name} receives msg: {msg}')

class Mediator:
    def contact(self, msg: str, person: Person): pass

class MediatorStructure(Mediator):
    def __init__(self): self.house_owner: 'HouseOwner' = None; self.tenant: 'Tenant' = None
    def set_house_owner(self, house_owner: 'HouseOwner'): self.house_owner = house_owner
    def set_tenant(self, tenant: 'Tenant'): self.tenant = tenant
    def contact(self, msg: str, person: 'Person'): 
        if not self.house_owner or not self.tenant: # Edge case check: Ensure both house_owner and tenant are set
            print("🟥 Error: Mediator is missing either house owner or tenant."); return 
        # 转发消息逻辑
        if person == self.house_owner and self.tenant: 
            self.tenant.receive_msg(msg)
        elif person == self.tenant and self.house_owner: 
            self.house_owner.receive_msg(msg)

# 测试用例
if __name__ == "__main__":
    mediator = MediatorStructure()

    # 初始化
    house_owner = HouseOwner("Tom", mediator)
    tenant = Tenant("Jerry", mediator)

    mediator.set_house_owner(house_owner)
    mediator.set_tenant(tenant)

    # 测试 #1: HouseOwner 给 Tenant 发送消息
    house_owner.contact("I have a house with a big swimming pool.")

    # 测试 #2: Tenant 给 HouseOwner 发送消息
    tenant.contact("Need a house with a big swimming pool.")

    # 🟥 Edge Case: Mediator without tenants or owners
    mediator_empty = MediatorStructure()
    empty_owner = HouseOwner("EmptyOwner", mediator_empty)
    empty_owner.contact("This should trigger an edge case warning.")

    # 测试 #3: 确认中介通信流程
    house_owner.contact("The house is available for viewing next week.")
    tenant.contact("Can we set up a visit next Thursday?")

    # 测试 #4: 测试多个房主和租户
    new_owner = HouseOwner("Alice", mediator)
    mediator.set_house_owner(new_owner)
    new_owner.contact("I have another house for rent.")
    tenant.contact("Is the second house available?")

    # 🟥 Edge Case: Tenant contacts without a set HouseOwner
    mediator_only_tenant = MediatorStructure()
    mediator_only_tenant.set_tenant(tenant)
    tenant.contact("Is there any available house?")

"""
问题描述：
实现一个房屋租赁中介系统，使用 Python 3 的面向对象编程原则。

要求：
1. 创建一个 `Person` 类，包含 `name` 属性和对 `Mediator` 对象的引用。
2. 实现继承于 `Person` 的 `HouseOwner` 和 `Tenant` 类，并包含 `contact` 和 `receive_msg` 方法。
3. 创建一个继承 `Mediator` 的 `MediatorStructure` 类，实现中介者模式来处理 `HouseOwner` 和 `Tenant` 间的消息通信。
4. 添加方法以设置 `HouseOwner` 和 `Tenant` 对象。
5. 确保实现边缘情况检测并提供详细的测试用例以验证功能。

保证所有类和方法使用正确的类型提示，代码结构清晰且易于扩展。
"""
