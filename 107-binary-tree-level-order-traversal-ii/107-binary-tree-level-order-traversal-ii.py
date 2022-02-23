# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(not root):
            return []
        l=[[root.val]]
        q=deque([root,-1])
        t=[]
        while(q):
            a=q.popleft()
            if(a==-1 and len(q)):
                l.append(t)
                t=[]
                q.append(-1)
            elif(a!=-1):
                if(a.left):
                    q.append(a.left)
                    t.append(a.left.val)
                if(a.right):
                    q.append(a.right)
                    t.append(a.right.val)
        return l[::-1]
            
        
        