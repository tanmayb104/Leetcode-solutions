class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans=[]
        s=set()
        for i in nums:
            if(i in s):
                ans.append(i)
            else:
                s.add(i)
        return ans
    
# 2 1 3 5 4
# 2 -1 3 5 4