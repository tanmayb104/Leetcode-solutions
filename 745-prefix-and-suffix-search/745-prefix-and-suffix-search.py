class WordFilter:

    def __init__(self, words: List[str]):
        self.trie={}
        self.weight_marker='$'
        w=self.weight_marker
        for idx, word in enumerate(words):
            word=word + '#'
            length=len(word)
            word+=word
            
            for i in range(length):
                curr=self.trie
                curr[w]=idx 
                for c in word[i:]:
                    if c not in curr:
                        curr[c]={}
                    curr=curr[c]                    
                    curr[w]=idx  # update the weight of substring                        
            

    def f(self, prefix: str, suffix: str) -> int:
        curr=self.trie
        for c in suffix + '#' + prefix:
            if c not in curr:
                return -1
            curr=curr[c]
        
        return curr[self.weight_marker] 