from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        c=Counter(s)
        s=sorted(c.keys(),key=lambda x:-c[x])
        ans=""
        for i in s:
            ans+=i*c[i]
        return ans
        