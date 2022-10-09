# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        l=[]
        def inorder(root):
            if(root):
                inorder(root.left)
                l.append(root.val)
                inorder(root.right)
        inorder(root)
        d={}
        for i in l:
            if(k-i in d):
                return True
            else:
                d[i]=1
        return False
        