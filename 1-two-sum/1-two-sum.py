from collections import Counter
class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        nums=[[n[i],i] for i in range(len(n))]
        nums.sort()
        l=0
        r=len(nums)-1
        while(l<r):
            if(nums[l][0]+nums[r][0]==target):
                return [nums[l][1],nums[r][1]]
            elif(nums[l][0]+nums[r][0]<target):
                l+=1
            else:
                r-=1
        
        
                