class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(2,len(nums)):    
            a=nums[i]
            b=nums[i-1]
            c=nums[i-2]
            if(a<b+c and b<a+c and c<a+b):
                return a+b+c
        return 0