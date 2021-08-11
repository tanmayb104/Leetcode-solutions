from collections import Counter
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c=Counter(nums)
        j=-1
        k=-1
        for i in range(len(nums)):
            if target-nums[i] in c.keys():
                if(nums[i]==target-nums[i]):
                    if(c[nums[i]]>1):
                        a=nums[i]
                        b=target-nums[i]
                        j=i
                else:
                    a=nums[i]
                    b=target-nums[i]
                    j=i
                    
        for i in range(len(nums)):
            if(nums[i]==b and j!=i):
                break
        return [i,j]
            
        
                