class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        l=[]
        for i in strs:
            l.append([i.count("0"),i.count("1")])
            
        @lru_cache(maxsize=None)
        def rec(m,n,i):
            if(m<0 or n<0):
                return -9999999999999
            if(i==len(strs)):
                return 0
            if(m==0 and n==0):
                return 0
            return max(rec(m,n,i+1),1+rec(m-l[i][0],n-l[i][1],i+1))
            
        return rec(m,n,0)