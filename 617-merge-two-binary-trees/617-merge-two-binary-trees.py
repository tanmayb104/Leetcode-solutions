# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if(not root1 and not root2):
            return None
        elif(not root1):
            return root2
        elif(not root2):
            return root1
        l1=deque([root1])
        l2=deque([root2])
        while(l1 and l2):
            a=l1.pop()
            b=l2.pop()
            if(a and b):
                a.val+=b.val
                if(a.left and b.left):
                    l1.append(a.left)
                    l2.append(b.left)
                elif(a.left):
                    pass
                elif(b.left):
                    a.left=b.left
                if(a.right and b.right):
                    l1.append(a.right)
                    l2.append(b.right)
                elif(a.right):
                    pass
                elif(b.right):
                    a.right=b.right
        return root1
                
            
        
        