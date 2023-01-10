# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if(not p and not q):
            return True
        elif(not p or not q):
            return False
        a1=[p]
        a2=[q]
        while(len(a1) and len(a2)):
            # print(a1,a2)
            p1=a1.pop()
            q1=a2.pop()
            if(p1.val!=q1.val):
                return False
            if(p1.right and q1.right):
                a1.append(p1.right)
                a2.append(q1.right)
            else:
                if(not p1.right and not q1.right):
                    pass
                else:
                    return False
                
            if(p1.left and q1.left):
                a1.append(p1.left)
                a2.append(q1.left)
            else:
                if(not p1.left and not q1.left):
                    pass
                else:
                    return False
        # print(a1,a2)
        return True
                