from collections import Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s=set(nums)
        ans=[]
        added=set()
        c=Counter(nums)
        if(0 in c):
            if(c[0]>=3):
                added.add((0,0,0))
                ans.append([0,0,0])
            c[0]=1
        for i in c.keys():
            if(c[i]>2):
                c[i]=2
        nums=[]
        for i in c.keys():
            nums+=[i]*c[i]
        # print(nums)
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if(-nums[i]-nums[j] in s):
                    a=[nums[i],nums[j],-nums[i]-nums[j]]
                    a.sort()
                    c1=Counter(a)
                    a=tuple(a)
                    flag=True
                    for k in c1.keys():
                        if(c1[k]>c[k]):
                            flag=False
                    if(a not in added and flag):
                        # print(c1)
                        added.add(a)
                        ans.append([nums[i],nums[j],-nums[i]-nums[j]])
        return ans
                    
        