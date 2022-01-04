class Solution:
    def per(self, nums, temp, ans, i, j, s):
        # print(temp)
        
        temp[i]=nums[j]
        for k in range(len(nums)):
            if(temp[k]==-11):
                self.per(nums,temp,ans,k,j+1,s)
        if(j==len(nums)-1):
            a=[i for i in temp]
            if(tuple(a) not in s):
                ans.append(a)
                s.add(tuple(a))
        temp[i]=-11
        
        
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        s=set()
        temp=[-11 for i in range(len(nums))]
        for i in range(len(nums)):
            self.per(nums,temp,ans,i,0,s)
        return ans
            
        