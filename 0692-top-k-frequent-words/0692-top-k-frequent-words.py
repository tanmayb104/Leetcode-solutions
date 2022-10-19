class Solution:
    def topKFrequent(self, w: List[str], k: int) -> List[str]:
        d={}
        for i in w:
            if(i in d):
                d[i]+=1
            else:
                d[i]=1
        l=[]
        for i in d:
            l.append([i,d[i]])
        l=sorted(l,key=lambda x:(-x[1],x[0]))
        ans=[]
        for i in range(k):
            ans.append(l[i][0])
        return ans