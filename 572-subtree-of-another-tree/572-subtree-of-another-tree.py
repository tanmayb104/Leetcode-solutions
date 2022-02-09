# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree1(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if(not root and not subRoot):
            return True
        elif(not root and subRoot):
            return False
        elif(root and not subRoot):
            return False        
        if(root.val==subRoot.val):
            return self.isSubtree1(root.left,subRoot.left) and self.isSubtree1(root.right,subRoot.right)
        return False
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        l=[root]
        m=False
        while(l):
            a=l.pop()
            # print(a.val)
            if(a.val==subRoot.val):
                m=m or self.isSubtree1(a,subRoot)
            if(a.left):
                l.append(a.left)
            if(a.right):
                l.append(a.right)
        return m
        
        
        