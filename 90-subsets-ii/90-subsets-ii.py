class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        l=[]
        nums.sort()
        def solve(nums,i,l,out):
            if(i==len(nums)):
                l.append(out)
                return
            solve(nums,i+1,l,out)
            solve(nums,i+1,l,out+[nums[i]])
        solve(nums,0,l,[])
        d={}
        ans=[]
        for i in l:
            t=tuple(i)
            if(t not in d):
                ans.append(i)
                d[t]=0
        return ans
        