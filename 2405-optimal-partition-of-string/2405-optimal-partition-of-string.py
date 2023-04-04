class Solution:
    def partitionString(self, s: str) -> int:
        d={}
        ans=0
        for i in range(len(s)):
            if(s[i] in d):
                ans+=1
                d={}
                d[s[i]]=1
            else:
                d[s[i]]=1
        return ans+1