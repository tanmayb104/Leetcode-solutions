from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums=Counter(nums)
        for i in nums.keys():
            if(nums[i]!=2):
                return i