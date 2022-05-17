# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        st1=[original]
        st2=[cloned]
        while(st1):
            a1=st1.pop()
            a2=st2.pop()
            if(a1==target):
                return a2
            if(a1.left):
                st1.append(a1.left)
                st2.append(a2.left)
            if(a1.right):
                st1.append(a1.right)
                st2.append(a2.right)
        