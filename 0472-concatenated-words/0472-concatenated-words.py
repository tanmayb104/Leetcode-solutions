class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        ddic = lambda: defaultdict(ddic)
        trie = ddic()
        
        for word in words:
            cur = trie
            for char in word:
                cur = cur[char]

            cur['end'] = True
        
        def isConcat(word, start):
            cur = trie
            for i in range(start, len(word)):
                char = word[i]
                if char not in cur:
                    return False
                cur = cur[char]

                if 'end' in cur:
                    if i + 1 == len(word):
                        return start != 0
                    
                    if isConcat(word, i + 1):
                        return True

            return False
            
        return [word for word in words if isConcat(word, 0)]