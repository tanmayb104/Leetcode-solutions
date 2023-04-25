class SmallestInfiniteSet:

    def __init__(self):
        self.mi=1
        self.s=set()
        

    def popSmallest(self) -> int:
        if(len(self.s)):
            mi=min(self.s)
            self.s.remove(mi)
            return mi
        self.mi+=1
        return self.mi-1

    def addBack(self, num: int) -> None:
        if(num>=self.mi):
            return
        else:
            self.s.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)