class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        m=max(max(nums),0)
        nums=list(set(nums))
        nums=[i for i in nums if i>0]
        n=len(nums)
        # print(nums)
        for i in range(n):
            if(nums[i]<=n):
                nums[abs(nums[i])-1]=-nums[i]
        flag=True
        for i in range(n):
            if(nums[i]>0):
                return(i+1)
                flag=False
        if(True):
            return(m+1)
        