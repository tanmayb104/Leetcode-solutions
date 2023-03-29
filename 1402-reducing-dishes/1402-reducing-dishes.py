class Solution:
    def maxSatisfaction(self, s: List[int]) -> int:
        s.sort(reverse=True)
        # print(s)
        ans=0
        p=0
        for i in s:
            if(p+i>=0):
                ans+=p+i
                p+=i
            else:
                break
            # print(i,p,ans)
        return ans