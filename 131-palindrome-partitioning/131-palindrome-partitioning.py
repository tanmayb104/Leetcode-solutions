class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def rec(s,l,i):
            # print(l)
            if(i==len(s)):
                ans.append(l.copy())
            for j in range(i+1,len(s)+1):
                t=s[i:j]
                if(t==t[::-1]):
                    l+=[t]
                    rec(s,l,j)
                    l.pop()
            
        ans=[]
        rec(s,[],0)
        return ans
        
        