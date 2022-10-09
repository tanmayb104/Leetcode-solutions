# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        d={}
        flag=False
        def inorder(root):
            nonlocal flag
            if(root):
                inorder(root.left)
                if(k-root.val in d):
                    flag=True
                else:
                    d[root.val]=1
                inorder(root.right)
        inorder(root)
        return flag
        