from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        minqueue = deque()

        # initialize the window
        for i in range(min(k, len(nums))):
            while minqueue and nums[minqueue[-1]] <= nums[i]: minqueue.pop()
            minqueue.append(i)

        res = [nums[minqueue[0]]]  # results

        for i in range(k, len(nums)):
            while minqueue and minqueue[0] <= i - k:  # clean up stale elements
                minqueue.popleft()
            while minqueue and nums[minqueue[-1]] <= nums[i]:  # kick out smaller ones
                minqueue.pop()
            minqueue.append(i)
            res.append(nums[minqueue[0]])  # guaranteed to be the max

        return res