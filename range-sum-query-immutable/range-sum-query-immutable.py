class NumArray:

    def __init__(self, nums: List[int]):
        pre=[0]
        for i in range(len(nums)):
            pre.append(pre[-1]+nums[i])
        self.pre=pre
        return 
        
        

    def sumRange(self, left: int, right: int) -> int:
        return self.pre[right+1]-self.pre[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)