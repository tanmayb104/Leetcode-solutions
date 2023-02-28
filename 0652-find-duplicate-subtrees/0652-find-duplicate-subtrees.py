# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        
        seen = collections.defaultdict(int)
        res = []
        
        def helper(node):
            if not node:
                return
            sub = tuple([helper(node.left), node.val, helper(node.right)])
            if sub in seen and seen[sub] == 1:
                res.append(node)
            seen[sub] += 1
            return sub
        
        helper(root)
        return res