from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        nums=sorted(c.keys(),key=lambda x:-c[x])
        return nums[:k]
        