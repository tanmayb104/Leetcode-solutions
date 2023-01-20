class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        for i in range(len(nums)-1,-1,-1):
            if(not len(ans)):
                ans.append([nums[i]])
            else:
                for j in range(len(ans)):
                    if(ans[j][0]>=nums[i]):
                        ans.append([nums[i]]+ans[j])
                ans.append([nums[i]])
        fans=[tuple(i) for i in ans]
        ans=set()
        for i in fans:
            if(i not in ans):
                ans.add(i)
        ans=list(ans)
        ans=sorted(ans,key=lambda x:len(x))
        # print(ans)
        for i in range(len(ans)):
            if(len(ans[i])==2):
                return ans[i:]
        