class Solution:
        
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        p=[i for i in nums[::-1]]
        for i in range(1,len(p)):
            p[i]+=p[i-1]
        p=p[::-1]
        
        @cache
        def rec(i,s):
            if(i==len(nums) and target==s):
                return 1
            elif(i==len(nums)):
                return 0
            elif(s-p[i]<=target and target<=s+p[i]):
                return rec(i+1,s-nums[i])+rec(i+1,s+nums[i])
            else:
                return 0 
        
        return rec(0,0)