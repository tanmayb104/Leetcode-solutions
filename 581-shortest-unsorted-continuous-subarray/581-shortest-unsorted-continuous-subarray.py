class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        a=sorted(nums)
        n=len(nums)
        ans=n
        for i in range(n):
            if(a[i]==nums[i]):
                ans-=1
            else:
                break
        for i in range(n-1,-1,-1):
            if(a[i]==nums[i]):
                ans-=1
            else:
                break
        return max(ans,0)