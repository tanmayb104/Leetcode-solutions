from collections import Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        se=set()
        for i in range(len(nums)):
            l=0
            h=len(nums)-1
            while(l<h):
                if(nums[i]+nums[l]+nums[h]>0):
                    h-=1
                elif(nums[i]+nums[l]+nums[h]<0):
                    l+=1
                else:
                    if(i!=l and l!=h and i!=h):
                        a=[nums[i],nums[l],nums[h]]
                        a.sort()
                        b=tuple(a)
                        if(b not in se):
                            se.add(b)
                            ans.append(a)
                    l+=1
                    h-=1
        return ans