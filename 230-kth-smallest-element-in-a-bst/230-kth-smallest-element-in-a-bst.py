# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:            
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k=k
        def inorder(root):
            if(root):
                inorder(root.left)
                self.k-=1
                if(self.k==0):
                    raise Exception(root.val)
                inorder(root.right)
        try:
            inorder(root)
        except Exception as e:
            return e