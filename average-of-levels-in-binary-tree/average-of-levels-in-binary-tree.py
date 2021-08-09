# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans=[]
        d=0
        avg=0
        co=0
        qu=deque()
        qu.append([root,0])
        while(qu):
            a,de=qu.popleft()
            if(de==d):
                avg+=a.val
                co+=1
            else:
                ans.append(avg/co)
                avg=a.val
                co=1
                d+=1
            if(a.left):
                qu.append([a.left,de+1])
            if(a.right):
                qu.append([a.right,de+1])
        ans.append(avg/co)
        return ans