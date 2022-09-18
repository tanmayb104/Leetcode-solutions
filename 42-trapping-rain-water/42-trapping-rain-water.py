class Solution:
    def trap(self, bars):
        if not bars or len(bars) < 3:
            return 0
        volume = 0
        left, right = 0, len(bars) - 1
        l_max, r_max = bars[left], bars[right]
        while left < right:
            l_max, r_max = max(bars[left], l_max), max(bars[right], r_max)
            if l_max <= r_max:
                volume += l_max - bars[left]
                left += 1
            else:
                volume += r_max - bars[right]
                right -= 1
        return volume
        