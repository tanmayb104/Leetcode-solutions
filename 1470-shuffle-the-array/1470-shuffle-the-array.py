class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l=[]
        for i in range(len(nums)//2):
            l+=[nums[i],nums[i+len(nums)//2]]
        return l