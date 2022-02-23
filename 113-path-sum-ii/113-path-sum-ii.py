# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if(not root):
            return []
        def rec(root,l,t):
            l.append(root.val)
            # print(root.val,l,t,ans)
            if(not root.left and not root.right and t==root.val):
                a=l.copy()
                ans.append(a)
            if(root.left):
                rec(root.left,l,t-root.val)
            if(root.right):
                rec(root.right,l,t-root.val)
            l.pop()
        ans=[]
        rec(root,[],targetSum)
        return ans
        