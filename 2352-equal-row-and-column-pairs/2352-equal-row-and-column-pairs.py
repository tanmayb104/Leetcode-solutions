class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        r={}
        for i in range(len(grid)):
            tu=tuple(grid[i])
            if(tu in r):
                r[tu]+=1
            else:
                r[tu]=1
        c={}
        for i in range(len(grid)):
            l1=[]
            for j in range(len(grid)):
                l1.append(grid[j][i])
            tu=tuple(l1)
            if(tu in c):
                c[tu]+=1
            else:
                c[tu]=1
        ans=0
        for i in r:
            if(i in c):
                ans+=r[i]*c[i]
        return ans
        