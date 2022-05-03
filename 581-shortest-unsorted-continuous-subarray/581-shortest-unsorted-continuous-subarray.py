class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        a=sorted(nums)
        n=len(nums)
        ans=n
        l=0
        r=n-1
        while(l<n and a[l]==nums[l]):
            l+=1
            ans-=1
        while(r>-1 and a[r]==nums[r]):
            r-=1
            ans-=1
        return max(ans,0)
        
                