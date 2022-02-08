# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        d=1
        q=deque([root,-1])
        if(not root):
            return 0
        while(q):
            # print(q)
            i=q.popleft()
            if(i==-1 and len(q)>=1):
                d+=1
                q.append(-1)
            elif(i==-1):
                break
            else:
                if(i.right):
                    q.append(i.right)
                if(i.left):
                    q.append(i.left)
        return d
        
        
        
        