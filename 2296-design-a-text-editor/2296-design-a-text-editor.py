class TextEditor:

    def __init__(self):
        self.pos=0
        self.text=""
        

    def addText(self, text: str) -> None:
        self.text=self.text[:self.pos]+text+self.text[self.pos:]
        self.pos+=len(text)
        

    def deleteText(self, k: int) -> int:
        pre=self.pos
        self.pos=max(0,self.pos-k)
        self.text=self.text[:self.pos]+self.text[pre:]
        return pre-self.pos
        
        

    def cursorLeft(self, k: int) -> str:
        self.pos=max(0,self.pos-k)
        return self.text[max(0,self.pos-10):self.pos]
        

    def cursorRight(self, k: int) -> str:
        self.pos=min(len(self.text),self.pos+k)
        return self.text[max(0,self.pos-10):self.pos]
        


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)