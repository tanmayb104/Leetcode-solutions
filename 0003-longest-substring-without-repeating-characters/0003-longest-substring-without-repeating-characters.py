class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        l=0
        r=0
        ans=0
        while(r<len(s)):
            if(s[r] not in d):
                d[s[r]]=1
                r+=1
                ans=max(ans,r-l)
            else:
                while(s[l]!=s[r]):
                    del d[s[l]]
                    l+=1
                del d[s[l]]
                l+=1
        return ans
                