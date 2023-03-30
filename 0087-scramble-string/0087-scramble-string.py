class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n != len(s2):
            return False
        if n == 0:
            return True
        elif n == 1:
            return s1 == s2
        else:
            memo = {}
            return self.isScrambleHelper(memo, s1, s2)

    def isScrambleHelper(self, memo: dict, s1: str, s2: str) -> bool:
        n = len(s1)
        result = False

        if n == 0:
            return True
        elif n == 1:
            return s1 == s2
        else:
            if (s1, s2) in memo:
                return memo[(s1, s2)]

            if s1 == s2:
                result = True
            else:
                for i in range(1, n):
                    result = (self.isScrambleHelper(memo, s1[:i], s2[:i]) and self.isScrambleHelper(memo, s1[i:], s2[i:])) or \
                             (self.isScrambleHelper(memo, s1[:i], s2[n - i:]) and self.isScrambleHelper(memo, s1[i:], s2[:n - i]))
                    if result:
                        break

            memo[(s1, s2)] = result
            return result