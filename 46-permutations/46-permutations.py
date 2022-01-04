class Solution:
    def per(self, nums, temp, ans, i, j):
        # print(temp)
        temp[i]=nums[j]
        for k in range(len(nums)):
            if(temp[k]==-11):
                self.per(nums,temp,ans,k,j+1)
        if(j==len(nums)-1):
            a=[i for i in temp]
            ans.append(a)
        temp[i]=-11
        
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        temp=[-11 for i in range(len(nums))]
        for i in range(len(nums)):
            self.per(nums,temp,ans,i,0)
        return ans
            
        