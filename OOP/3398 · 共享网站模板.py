from typing import Dict
class Demand: 
    def __init__(self, user, content): # Extrinsic/ spesific 
        self.user = user; self.content = content 
        
class Template: 
    def create(self, demand: Demand): pass 

class ConcreteTemplate(Template): 
    def __init__(self, type): # Intrinsic/ shared 
        self.type = type 

    def create(self, demand: Demand): # Output Extrinsic & Intrinsic
        tmp = ", ".join(f"{k}: {v}" for k, v in demand.content) 
        print(f"Template(type = {self.type}, user = {demand.user}, content = {tmp})")

class WebsiteFactory:
    # 造/重用 template
    def __init__(self):
        self.pool =  {} 
    def get_template(self, type: str) -> ConcreteTemplate:
        if type not in self.pool:
            print(f"Creating new template of type: {type}")
            self.pool[type] = ConcreteTemplate(type)
        return self.pool[type] 
    def get_size(self) -> int:
        return len(self.pool) 

def run_tests():
    factory = WebsiteFactory()

    # Test 1: Tom creates a blog website
    tom_demand = Demand("Tom", {"Title": "Tom's Blog", "Desc": "Welcome to My Blog."})
    blog_template = factory.get_template("Blog")
    blog_template.create(tom_demand)

    # Test 2: Jerry creates a news website
    jerry_demand = Demand("Jerry", {"Title": "News Website", "Desc": "Free for Everyone!"})
    news_template = factory.get_template("News")
    news_template.create(jerry_demand)

    # Test 3: Mike uses a news template with custom content
    mike_demand = Demand("Mike", {"Title": "Copy a News Website", "Content": "Copy from Jerry's."})
    news_template.create(mike_demand)  # Reuses the same "News" template

    # Test 4: Verify the size of the template pool
    print(f"\nSize of Template Pool: {factory.get_size()}")  # Expected: 2


# Execute tests
if __name__ == "__main__":
    run_tests()
 