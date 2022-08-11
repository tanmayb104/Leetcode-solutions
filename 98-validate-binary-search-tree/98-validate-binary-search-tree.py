# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        l=[]
        def inorder(root):
            if(root):
                inorder(root.left)
                l.append(root.val)
                inorder(root.right)
        inorder(root)
        a=[i for i in l]
        a.sort()
        if(a==l and len(set(l))==len(l)):
            return True
        return False