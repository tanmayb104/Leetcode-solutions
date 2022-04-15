class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m=1
        ma=1
        for i in range(len(nums)):
            if(m>i):
                m=max(m,ma+nums[i])
                ma+=1
            else:
                return False
        return True
            