class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        arr=[0 for i in range(N+1)]
        g={}
        for i in trust:
            arr[i[1]]+=1
            if(i[0] in g):
                g[i[0]].append(i[1])
            else:
                g[i[0]]=[i[1]]
        ans=[]
        for i in range(N,-1,-1):
            if(arr[i]==N-1):
                ans.append(i)
        for i in ans:
            if(i not in g):
                return i
        return -1