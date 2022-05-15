# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        s=0
        d=deque([root,-1])
        while(d):
            a=d.popleft()
            if(a==-1 and len(d)):
                s=0
                d.append(-1)
            elif(a!=-1):
                s+=a.val
                if(a.right):
                    d.append(a.right)
                if(a.left):
                    d.append(a.left)
        return(s)
        
        