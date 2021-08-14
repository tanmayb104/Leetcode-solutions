class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans=set()
        s=set()
        for i in nums:
            if(i in s):
                ans.add(i)
            else:
                s.add(i)
        return list(ans)