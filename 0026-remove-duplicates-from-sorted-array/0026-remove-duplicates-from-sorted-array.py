class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=0
        for i in range(1,len(nums)):
            if(nums[i]==nums[l]):
                nums[i]=""
            else:
                nums[l+1]=nums[i]
                l+=1
        return l+1