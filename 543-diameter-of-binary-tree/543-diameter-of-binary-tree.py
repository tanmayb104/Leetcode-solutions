# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


    
    
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def calc(node):
            nonlocal m
            if(node.right and node.left):
                le=1+calc(node.left)
                ri=1+calc(node.right)
                m=max(m,le+ri)
                return max(le,ri)
            elif(node.left):
                le=1+calc(node.left)
                m=max(m,le)
                return le
            elif(node.right):
                ri=1+calc(node.right)
                m=max(m,ri)
                return ri
            return 0
        m=0
        calc(root)
        return m