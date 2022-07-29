class Solution:
    def findAndReplacePattern(self, w: List[str], p: str) -> List[str]:
        
        def check(a,b):
            d={}
            for i in range(len(a)):
                if(a[i] in d):
                    if(d[a[i]]!=b[i]):
                        return False
                else:
                    d[a[i]]=b[i]
            return True
        
        ans=[]
        for i in range(len(w)):
            if(check(p,w[i]) and check(w[i],p)):
                ans.append(w[i])
        return ans