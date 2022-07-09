from heapq import *
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        h=[]
        heapify(h)
        ans=[0 for i in range(len(nums))]
        ans[0]=nums[0]
        heappush(h,[-ans[0],0])
        i=1
        while(i<len(nums)):
            a,b=heappop(h)
            if(b>=i-k):
                ans[i]=ans[b]+nums[i]
                heappush(h,[-ans[i],i])
                if(b!=i-k):
                    heappush(h,[a,b])
                i+=1
        # print(ans)
        return ans[-1]
            