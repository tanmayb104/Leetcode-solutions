class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # if(len(nums)<3):
        #     return False
        mi=[[nums[0],0]]
        for i in range(1,len(nums)):
            if(nums[i]<mi[-1][0]):
                mi.append([nums[i],i])
            else:
                mi.append(mi[-1])
        ma=[[nums[-1],len(nums)-1]]
        for i in range(len(nums)-2,-1,-1):
            if(nums[i]>ma[-1][0]):
                ma.append([nums[i],i])
            else:
                ma.append(ma[-1])
        ma=ma[::-1]
        # print(nums)
        # print(mi)
        # print(ma)
        for i in range(1,len(nums)-1):
            if(mi[i][0]<nums[i]<ma[i][0]):
                return True
        return False
        
                
        