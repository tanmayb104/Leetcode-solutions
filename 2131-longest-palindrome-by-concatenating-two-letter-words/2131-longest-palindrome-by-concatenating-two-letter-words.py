class Solution(object):
    def longestPalindrome(self, words):
        wc = collections.Counter(words)
        aa = 0  
        center = 0
        abba = 0 
        for w, c in wc.items():
            if w[0] == w[1]:
                aa += c // 2 * 2 
                if c % 2 == 1: center = 2
            else:
                abba += min(wc[w], wc[w[::-1]]) * 0.5  
        return aa * 2 + int(abba) * 4 + center