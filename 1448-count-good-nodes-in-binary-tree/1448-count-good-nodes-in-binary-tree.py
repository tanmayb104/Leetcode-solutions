# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans=0
        def rec(root,ma):
            nonlocal ans
            if(root):
                if(ma<=root.val):
                    ans+=1
                m=max(ma,root.val)
                rec(root.right,m)
                rec(root.left,m)
        rec(root,-9999999)
        return ans