# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        l=[root]
        while(l):
            a=l.pop()
            a.left,a.right=a.right,a.left
            if(a.left):
                l.append(a.left)
            if(a.right):
                l.append(a.right)
        return root