class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        ans=""
        for i in s:
            ans+=i[::-1]
            ans+=" "
        return ans[:-1]