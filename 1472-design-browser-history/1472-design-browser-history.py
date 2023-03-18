class Node:
    def __init__(self, url, prev=None, forw=None):
        self.url=url
        self.prev=prev
        self.forw=forw

class BrowserHistory:

    def __init__(self, homepage: str):
        self.l=Node(homepage)

    def visit(self, url: str) -> None:
        node=Node(url,self.l)
        self.l.forw=node
        self.l=self.l.forw
        

    def back(self, steps: int) -> str:
        while(steps and self.l.prev):
            steps-=1
            self.l=self.l.prev
        return self.l.url
        

    def forward(self, steps: int) -> str:
        while(steps and self.l.forw):
            steps-=1
            self.l=self.l.forw
        return self.l.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)