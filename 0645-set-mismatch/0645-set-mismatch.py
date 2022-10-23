class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            if(i in d):
                ans=[i]
            else:
                d[i]=1
        for i in range(1,len(nums)+1):
            if(i not in d):
                ans+=[i]
        return ans