class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[defaultdict(int) for _ in range(n)]
        res=0
        for i in range(n):
            for j in range(i):
                diff=nums[i]-nums[j]
                dp[i][diff]+=(1+dp[j][diff])
                res+=dp[j][diff]

        return res  