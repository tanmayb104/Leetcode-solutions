class Solution:
    def minimizeArrayValue(self, num: List[int]) -> int:
        l=min(num)
        r=max(num)
        while(l<r):
            nums=num.copy()
            mid=(l+r)//2
            flag=True
            for i in range(len(nums)-1,-1,-1):
                if(nums[i]>mid and i!=0):
                    nums[i-1]+=nums[i]-mid
                    nums[i]=mid
                elif(nums[i]>mid and i==0):
                    flag=False
            # print(l,mid,r,nums)
            if(flag):
                r=mid
            else:
                l=mid+1
        return l