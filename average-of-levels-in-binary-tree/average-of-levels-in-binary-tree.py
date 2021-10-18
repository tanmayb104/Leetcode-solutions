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
        avg=0
        co=0
        qu=deque()
        qu.append(root)
        qu.append(-1)
        while(qu):
            a=qu.popleft()
            if(a!=-1):
                avg+=a.val
                co+=1
                if(a.left):
                    qu.append(a.left)
                if(a.right):
                    qu.append(a.right)
            else:
                ans.append(avg/co)
                avg=0
                co=0
                if(qu):
                    qu.append(-1)
        return ans