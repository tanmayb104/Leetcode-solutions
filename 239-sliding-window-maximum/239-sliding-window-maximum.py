from heapq import *
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        nums=[-i for i in nums]
        ans=[]
        l=0
        r=0
        d={}
        h=[]
        heapify(h)
        while(r<k):
            d[nums[r]]=r
            heappush(h,nums[r])
            r+=1
        a=heappop(h)
        ans.append(-a)
        if(d[a]!=l):
            heappush(h,a)
        while(r<len(nums)):
            l+=1
            d[nums[r]]=r
            heappush(h,nums[r])
            # print(ans,h,l,r)
            while(True):
                a=heappop(h)
                if(d[a]==l):
                    break
                elif(d[a]>l):
                    heappush(h,a)
                    break
            ans.append(-a)
            r+=1
        return ans
            
            
        