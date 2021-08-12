class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a=1
        c=0
        for i in nums:
            if(i):
                a*=i
            else:
                c+=1
        ans=[]
        for i in nums:
            if(i):
                if(c):
                    ans.append(0)
                else:
                    ans.append(a//i)
            else:
                if(c-1):
                    ans.append(0)
                else:
                    ans.append(a)
        return ans