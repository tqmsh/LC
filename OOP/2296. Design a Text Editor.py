class TextEditor:
    def __init__(self):
        self.l = []; self.r = []
        # abc | de
        # l = [abc]
        # r = [ed]
    def addText(self, text: str): self.l.extend(text)
    def deleteText(self, k: int) -> int:
        amt = min(len(self.l), k)
        for _ in range(amt): self.l.pop()
        return amt
    def cursorLeft(self, k: int) -> str:
        amt = min(len(self.l), k)
        for _ in range(amt): self.r.append(self.l.pop())
        return "".join(self.l[-10:]) # Last 10 element of l
    def cursorRight(self, k: int) -> str:
        amt = min(len(self.r), k)
        for _ in range(amt): self.l.append(self.r.pop())
        return "".join(self.l[-10:])        


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)