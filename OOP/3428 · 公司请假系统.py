# 责任链模式属于行为型模式。它是将链中每一个节点看作是一个对象，每个节点处理的请求均不同，且内部自动维护一个下一节点对象。
# 当一个请求从链式的首端发出时，会沿着链的路径依次传递给每一个节点对象，直至有对象处理这个请求为止。

class Request:
    def __init__(self, type: str, content: str, num: int): self.type = type; self.content = content; self.num = num
    def __str__(self): return f"Request(type = {self.type}, content = {self.content}, num = {self.num})"

class Handler:
    def __init__(self): self.nxt_handler: Handler = None
    def set_nxt_handler(self, nxt_handler: 'Handler'): self.nxt_handler = nxt_handler
    def do_handler(self, request: Request): pass

class LineManager(Handler):
    def do_handler(self, request: Request): 
        if request.num <= 3: print(f"==========\nLine Manager: {request} accepted, end")
        else:
            print(f"==========\nLine Manager: {request} accepted, forwarding")
            if self.nxt_handler: self.nxt_handler.do_handler(request)
            else: print("==========\nNext handler DNE")

class DepartmentManager(Handler):
    def do_handler(self, request: Request): 
        if 3 < request.num <= 7: print(f"==========\nDepartment Manager: {request} accepted, end")
        else:
            print(f"==========\nDepartment Manager: {request} accepted, forwarding")
            if self.nxt_handler: self.nxt_handler.do_handler(request)
            else: print("==========\nNext handler DNE")

class GeneralManager(Handler):
    def do_handler(self, request: Request): 
        print(f"==========\nGeneral Manager: {request} accepted, end")


# 测试代码 Test Cases
def test_chain_of_responsibility():
    # Initialization
    line_manager = LineManager(); department_manager = DepartmentManager(); general_manager = GeneralManager()
    line_manager.set_nxt_handler(department_manager); department_manager.set_nxt_handler(general_manager)

    # Test #1, functionality when request.num <= 3
    request1 = Request(type="Leave", content="Leave application for 2 days", num=2)
    line_manager.do_handler(request1)  # Expected to be handled by Line Manager

    # Test #2, functionality when 3 < request.num <= 7
    request2 = Request(type="Leave", content="Leave application for 5 days", num=5)
    line_manager.do_handler(request2)  # Expected to be handled by Department Manager
    
    # Test #3, functionality when request.num > 7
    request3 = Request(type="Leave", content="Leave application for 10 days", num=10)
    line_manager.do_handler(request3)  # Expected to be handled by General Manager

    # 🟥 Edge Case: Request with num = 0 (an edge case)
    request4 = Request(type="Leave", content="Leave application for 0 days", num=0)
    line_manager.do_handler(request4)  # Expected to be handled by Line Manager


# Execute tests
test_chain_of_responsibility()
