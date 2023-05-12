class Solution:
    def mostPoints(self, q: List[List[int]]) -> int:
        def rec(i):
            if(i in d):
                return d[i]
            if(i<len(q)):
                b=rec(i+1)
                a=rec(i+q[i][1]+1)+q[i][0]
                d[i]=max(a,b)
                return d[i]
            return 0
        d={}
        return rec(0)