class TrieNode:
    
    def __init__(self, val: str = None, parent: Optional['TrieNode'] = None):
        self.children = {}
        self.val = val
        self.parent = parent
        self.word = None
        

class Trie:
    
    def __init__(self):
        self.root = TrieNode()
    
    
    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(val=c, parent=node)
            node = node.children[c]
        node.word = word
        
    
    def prune(self, node: TrieNode) -> None:
        node.word = None
        child = node
        parent = child.parent
        while parent and len(child.children) == 0:
            del parent.children[child.val]
            child = parent
            parent = parent.parent
        
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.addWord(word)
        
        res = []
        m, n = len(board), len(board[0])
        seen = set()
        
        def dfs(i, j, node) -> None:
            if (i < 0 or i == m or j < 0 or j == n or
                (i, j) in seen or board[i][j] not in node.children):
                return
            seen.add((i, j))
            node = node.children[board[i][j]]
            
            if node.word:
                res.append(node.word)
                trie.prune(node)

            if len(node.children) == 0:
                seen.remove((i, j))
                return

            dfs(i + 1, j, node)
            dfs(i - 1, j, node)
            dfs(i, j + 1, node)
            dfs(i, j - 1, node)
            
            seen.remove((i, j))
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, trie.root)
        
        return res