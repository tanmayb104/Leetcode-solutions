# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if(not root):
            return root
        lca=root
        if p.val>q.val:
            p,q=q,p
        while(p.val>lca.val or q.val<lca.val):
            if(p.val>lca.val):
                lca=lca.right
            if(q.val<lca.val):
                lca=lca.left
        return lca