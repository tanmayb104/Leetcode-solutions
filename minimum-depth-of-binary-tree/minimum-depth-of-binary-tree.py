# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans=99999999999999
        d=0
        qu=deque()
        qu.append([root,0])
        while(qu):
            a,de=qu.pop()
            if(a.left):
                qu.append([a.left,de+1])
            if(a.right):
                qu.append([a.right,de+1])
            if(not a.left and not a.right):
                ans=min(ans,de+1)
        return ans