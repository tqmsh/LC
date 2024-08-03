class ListNode:
    def __init__(self, cnt=0, val=0, next=None, pre=None):
        self.val = val
        self.cnt = cnt  # 模版基础上新加的
        self.next = next
        self.pre = pre

class AllOne:
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode(float('inf'))
        self.head.next = self.tail
        self.tail.pre = self.head
        self.mp: dict[str, ListNode] = {}  # k -> node (val = k, cnt = v/频率)

    def swap(self, a, b, c, d):  # a <-> b <-> c <-> d => a <-> c <-> b <-> d
        a.next = c
        c.pre, c.next = a, b
        b.pre, b.next = c, d
        d.pre = b
        return (a, b, c, d)

    def inc(self, k: str):
        if k not in self.mp:  # head <-> node <-> head.next
            node = ListNode(1, k, self.head.next, self.head)
            self.head.next.pre = node
            self.head.next = node
            self.mp[k] = node
        else:
            node = self.mp[k]
            node.cnt += 1
            while node.next != self.tail and node.cnt > node.next.cnt:  # 维持顺序, 对换 node & node.next
                _, _, node, _ = self.swap(node.pre, node, node.next, node.next.next)

    def dec(self, k: str):
        if k in self.mp:
            node = self.mp[k]
            node.cnt -= 1
            if node.cnt == 0:  # node.pre <-> node <-> node.next => node.pre <-> node.next
                node.pre.next = node.next
                node.next.pre = node.pre
                del self.mp[k]
            else:
                while node.pre != self.head and node.cnt < node.pre.cnt:  # 维持顺序, 对换 node.pre & node
                    _, node, _, _ = self.swap(node.pre.pre, node.pre, node, node.next)

    def getMaxKey(self) -> str:
        if self.tail.pre != self.head:
            return self.tail.pre.val
        return ''

    def getMinKey(self) -> str:
        if self.head.next != self.tail:
            return self.head.next.val
        return ''

def test_AllOne():
    obj = AllOne()
    obj.inc("a")
    obj.inc("b")
    obj.inc("b")
    obj.inc("c")
    obj.inc("c")
    obj.inc("c")
    assert obj.getMaxKey() == "c"
    assert obj.getMinKey() == "a"
    obj.dec("c")
    obj.dec("c")
    obj.dec("c")
    assert obj.getMaxKey() == "b"
    assert obj.getMinKey() == "a"
    obj.dec("a")
    assert obj.getMinKey() == "b"
    print("All tests passed.")

test_AllOne()
