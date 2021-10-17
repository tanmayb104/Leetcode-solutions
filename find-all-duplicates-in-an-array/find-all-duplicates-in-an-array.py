class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s=[]
        for i in range(len(nums)):
            # print(nums)
            if(nums[abs(nums[i])-1]<0):
                s.append(abs(nums[i]))
            else:
                nums[abs(nums[i])-1]*=-1
                
        return s
    
# 2 1 3 5 4
# 2 -1 3 5 4