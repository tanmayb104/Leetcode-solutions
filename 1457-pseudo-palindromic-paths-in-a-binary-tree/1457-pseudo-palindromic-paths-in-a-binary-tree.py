# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        ans=0
        def dfs(root,d):
            nonlocal ans
            if(root.val in d):
                d[root.val]+=1
            else:
                d[root.val]=1
            if(not root.left and not root.right):
                a=0
                s=0
                for i in d:
                    s+=d[i]
                    if(d[i]%2==1):
                        a+=1
                if((s%2==0 and a==0) or (s%2==1 and a==1)):
                    ans+=1
            if(root.left):
                dfs(root.left,d)
            if(root.right):
                dfs(root.right,d)
            d[root.val]-=1
            
        dfs(root,{})
        return ans