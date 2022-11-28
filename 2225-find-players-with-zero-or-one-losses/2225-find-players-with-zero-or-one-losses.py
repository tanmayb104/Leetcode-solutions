class Solution:
    def findWinners(self, m: List[List[int]]) -> List[List[int]]:
        d={}
        for i in m:
            if(i[1] in d):
                d[i[1]]-=1
            else:
                d[i[1]]=-1
            if(i[0] not in d):
                d[i[0]]=0
        ans=[[],[]]
        for i in d:
            if(d[i]==0):
                ans[0].append(i)
            elif(d[i]==-1):
                ans[1].append(i)
        ans[0].sort()
        ans[1].sort()
        return ans
        