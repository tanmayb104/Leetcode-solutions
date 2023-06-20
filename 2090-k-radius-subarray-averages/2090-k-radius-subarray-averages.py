class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        su=0
        le=0
        for i in range(len(nums)):
            su+=nums[i]
            le+=1
            if(le>2*k+1):
                su-=nums[i-2*k-1]
                le-=1
            if(le==2*k+1):
                ans.append(su//(2*k+1))
            else:
                ans.append(-1)
        return ans[k:]+ans[:k]