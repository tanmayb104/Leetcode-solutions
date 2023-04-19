class Solution:
    def longestZigZag(self, root):
        def dfs(node):
            if not node:
                return [-1, -1, -1]
            left_subtree, right_subtree = dfs(node.left), dfs(node.right)
            return [
                left_subtree[1] + 1, 
                right_subtree[0] + 1, 
                max(left_subtree[1] + 1, right_subtree[0] + 1, left_subtree[2], right_subtree[2])
            ]
        return dfs(root)[-1]