# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if(not root):
            return None
        head=TreeNode()
        ans=head
        def rec(root):
            nonlocal head
            if(root):
                if(root.left):
                    rec(root.left)
                head.right=TreeNode(root.val)
                head=head.right
                if(root.right):
                    rec(root.right)
            return
        rec(root)
        return ans.right