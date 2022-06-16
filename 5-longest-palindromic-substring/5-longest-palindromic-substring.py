class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=s[0]
        for i in range(len(s)):
            p=s[i]
            l=i-1
            r=i+1
            while(l>-1 and r<len(s)):
                p=s[l]+p+s[r]
                if(s[l]==s[r]):
                    if(len(ans)<len(p)):
                        ans=p
                else:
                    break
                l-=1
                r+=1
        for i in range(len(s)-1):
            p=s[i]+s[i+1]
            if(s[i]==s[i+1]):
                if(len(ans)<len(p)):
                    ans=p
            else:
                continue
            l=i-1
            r=i+2
            while(l>-1 and r<len(s)):
                # print(p,i,l,r)
                p=s[l]+p+s[r]
                if(s[l]==s[r]):
                    if(len(ans)<len(p)):
                        ans=p
                else:
                    break
                l-=1
                r+=1
        return ans
                        