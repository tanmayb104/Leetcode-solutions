class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l=[i+1 for i in range(n)]
        a=-1
        while(len(l)>1):
            a+=k
            a%=len(l)
            l.pop(a)
            a-=1
            # print(l)
        return l[0]