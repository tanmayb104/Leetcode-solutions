class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans=[]
        even=0
        for i in nums:
            if(i%2==0):
                even+=i
        for i in queries:
            if(nums[i[1]]%2==0):
                if(i[0]%2==0):
                    even+=i[0]
                    ans.append(even)
                    nums[i[1]]+=i[0]
                else:
                    even-=nums[i[1]]
                    ans.append(even)
                    nums[i[1]]+=i[0]
            else:
                if(i[0]%2==1):
                    even+=i[0]+nums[i[1]]
                    ans.append(even)
                    nums[i[1]]+=i[0]
                else:
                    ans.append(even)
                    nums[i[1]]+=i[0]
        return ans