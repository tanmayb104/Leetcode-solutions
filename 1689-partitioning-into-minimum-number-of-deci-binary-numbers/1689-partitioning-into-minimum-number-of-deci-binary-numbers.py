class Solution:
    def minPartitions(self, n: str) -> int:
        m=0
        for i in n:
            m=max(m,int(i))
        return(m)