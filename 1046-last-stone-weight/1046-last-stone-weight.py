from heapq import *
class Solution:
    def lastStoneWeight(self, s: List[int]) -> int:
        s=[-i for i in s]
        heapify(s)
        while(len(s)>1):
            a=heappop(s)
            b=heappop(s)
            if(a==b):
                continue
            else:
                heappush(s,-abs(a-b))
        if(len(s)):
            return -heappop(s)
        return 0
                