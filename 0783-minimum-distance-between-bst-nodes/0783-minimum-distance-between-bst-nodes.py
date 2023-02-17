# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.ans=999999999999999999
        self.prev=-9999999999999
        def rec(node):
            if(node.left):
                rec(node.left)
            self.ans=min(self.ans,node.val-self.prev)
            self.prev=node.val
            if(node.right):
                rec(node.right)
        rec(root)
        return self.ans