class Solution:
    def solve(self, start_stick, end_stick, cuts, left, right, dp):
        if left > right:
            return 0

        if dp[left][right] != -1:
            return dp[left][right]

        cost = float('inf')

        for i in range(left, right + 1):
            left_cost = self.solve(start_stick, cuts[i], cuts, left, i - 1, dp)
            right_cost = self.solve(cuts[i], end_stick, cuts, i + 1, right, dp)
            curr_cost = (end_stick - start_stick) + left_cost + right_cost
            cost = min(cost, curr_cost)

        dp[left][right] = cost
        return cost

    def minCost(self, n, cuts):
        dp = [[-1] * len(cuts) for _ in range(len(cuts))]
        cuts.sort()
        return self.solve(0, n, cuts, 0, len(cuts) - 1, dp)