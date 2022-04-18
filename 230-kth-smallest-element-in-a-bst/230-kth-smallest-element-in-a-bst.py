# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root,l):
        if(root):
            self.inorder(root.left,l)
            l.append(root.val)
            self.inorder(root.right,l)
            
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l=[]
        self.inorder(root,l)
        return l[k-1]