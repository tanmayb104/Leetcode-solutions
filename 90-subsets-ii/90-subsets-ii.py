class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        s=set(tuple([]))
        l=[]
        nums.sort()
        def solve(nums,i,l,out,s):
            t=tuple(out)
            if(i==len(nums) and t not in s):
                l.append(out)
                s.add(t)
                return
            elif(i==len(nums)):
                return
            solve(nums,i+1,l,out,s)
            solve(nums,i+1,l,out+[nums[i]],s)
        solve(nums,0,l,[],set())
        return l
        