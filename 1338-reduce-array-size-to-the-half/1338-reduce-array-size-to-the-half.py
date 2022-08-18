from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n=len(arr)
        c=Counter(arr)
        l=[[c[i],i] for i in c.keys()]
        l.sort(reverse=True)
        ans=0
        p=n
        i=0
        while(p>n//2):
            p-=l[i][0]
            i+=1
            ans+=1
        return ans