class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        for i in range(1,len(gain)):
            gain[i]+=gain[i-1]
        return max(max(gain),0)