class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        res, mod = 0, 1000000007
        l, r = 0, len(nums) - 1
        pre = [1]
        for i in range(1, len(nums) + 1):
            pre.append((pre[-1] << 1) % mod)
                
        nums.sort()
        
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res = (res + pre[r - l]) % mod
                l += 1

        return res