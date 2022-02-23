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
            ans[-1].append(root.val)
            # print(root.val,l,t,ans)
            if(not root.left and not root.right and t==root.val):
                ans.append(ans[-1].copy())
            if(root.left):
                rec(root.left,l,t-root.val)
            if(root.right):
                rec(root.right,l,t-root.val)
            ans[-1].pop()
        ans=[[]]
        rec(root,[],targetSum)
        return ans[:-1]
        