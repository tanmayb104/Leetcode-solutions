class StockSpanner:

    def __init__(self):
        self.st=[]
        

    def next(self, p: int) -> int:
        if(not self.st or self.st[-1][0]>p):
            self.st.append([p,1])
            return 1
        else:
            a=1
            while(self.st and self.st[-1][0]<=p):
                a+=self.st.pop()[1]
            self.st.append([p,a])
            return a


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)