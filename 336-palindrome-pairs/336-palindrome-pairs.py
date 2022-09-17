class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def isPalindrome(s):
            start = 0
            end = len(s) - 1

            while( start < end ):
                if( s[ start ] != s[ end ] ):
                    return False
                start += 1
                end -= 1
            return True

        results = set()
        reversedWords = { word[::-1]: index for index, word in enumerate(words) }

        for i, word in enumerate(words):
            for j in range(0,len(word)+1):
                prefix = word[:j]
                pfremain = word[j:]
                if prefix in reversedWords and isPalindrome(pfremain) and reversedWords[prefix] != i:
                    results.add((i,reversedWords[prefix]))
            for j in range(len(word), -1, -1):
                suffix = word[j:]
                sfremain = word[:j]
                if suffix in reversedWords and isPalindrome(sfremain) and reversedWords[suffix] != i:
                    results.add((reversedWords[suffix],i))
        return results