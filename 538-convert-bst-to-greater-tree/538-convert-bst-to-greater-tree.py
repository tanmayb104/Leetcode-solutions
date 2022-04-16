# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from bisect import bisect
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if(not root):
            return None
        a=0
        def rec(root):
            nonlocal a
            # print("sadasd",a,root.val)
            if(root.left and root.right):
                rec(root.right)
                root.val+=a
                a=root.val
                rec(root.left)
            elif(root.left):
                root.val+=a
                a=root.val
                rec(root.left)
            elif(root.right):
                rec(root.right)
                root.val+=a
                a=root.val
            else:
                root.val+=a
                a=root.val
            # print(a,root.val)
        
        rec(root)
        return root
            