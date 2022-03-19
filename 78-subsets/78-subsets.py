class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l=[]
        def solve(nums,i,l,out):
            if(i==len(nums)):
                l.append(out)
                return
            solve(nums,i+1,l,out)
            solve(nums,i+1,l,out+[nums[i]])
        solve(nums,0,l,[])
        return l