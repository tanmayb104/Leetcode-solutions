class Solution:
        
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def rec(i,s):
            if((i,s) not in d):
                if(i==len(nums) and target==s):
                    d[(i,s)]=1
                elif(i==len(nums)):
                    d[(i,s)]=0
                else:
                    d[(i,s)]=rec(i+1,s-nums[i])+rec(i+1,s+nums[i])
            return d[(i,s)]
        
        d={}
        d[(0,0)]=rec(0,0)
        return d[(0,0)]
        
        