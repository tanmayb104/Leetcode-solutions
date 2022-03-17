from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        l=0
        r=0
        q=deque([])
        while(r<k):
            while(q and nums[q[-1]]<nums[r]):
                q.pop()
            q.append(r)
            r+=1
        while(r<=len(nums)):
            # print(q,l)
            while(q[0]<l):
                q.popleft()
            ans.append(nums[q[0]])
            while(q and r<len(nums) and nums[q[-1]]<nums[r]):
                q.pop()
            q.append(r)
            l+=1
            r+=1
        return ans
            
                
        
            
            
        