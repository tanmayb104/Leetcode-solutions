from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=Counter(nums)
        n=len(nums)
        for i in c.keys():
            if(c[i]>n//2):
                return i