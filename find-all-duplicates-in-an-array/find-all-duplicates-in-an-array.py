class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s=set()
        for i in range(len(nums)):
            if(nums[i]-1>=0):
                # print(nums[i]-1)
                if(nums[nums[i]-1]<0):
                    s.add(nums[i])
                else:
                    nums[nums[i]-1]-=9999999
            else:
                a=nums[i]-1+9999999
                # print(a)
                if(nums[a]<0):
                    s.add(a+1)
                else:
                    nums[a]-=9999999
                
        return list(s)
    
# 2 1 3 5 4
# 2 -1 3 5 4