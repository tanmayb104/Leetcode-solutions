# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        l1=[]
        l2=[]
        def dfs(root,t):
            nonlocal l1
            if(root==t):
                l1.append(root)
                raise Exception(l1)
            if(root.left):
                l1.append(root)
                dfs(root.left,t)
                l1.pop()
            if(root.right):
                l1.append(root)
                dfs(root.right,t)
                l1.pop()
        try:
            dfs(root,p)
        except Exception as e:
            l2=[i for i in l1]
            l1=[]
        try:
            dfs(root,q)
        except:
            pass
        prev=-1
        # print(l1,l2)
        for i in range(min(len(l1),len(l2))):
            if(l1[i]!=l2[i]):
                return prev
            prev=l1[i]
        return prev