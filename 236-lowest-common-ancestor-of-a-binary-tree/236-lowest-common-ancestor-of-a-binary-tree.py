# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def rec(root):
            if(not root):
                return False
            l=rec(root.left)
            r=rec(root.right)
            if(l and r):
                return root
            elif((root==p or root==q) and (l or r)):
                return root
            elif(root==p or root==q):
                return True
            else:
                return l or r
        return rec(root)