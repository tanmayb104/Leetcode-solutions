# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if(not root):
            return 0
        st=[[root,1]]
        ans=0
        while(st):
            a,d=st.pop()
            ans=max(ans,d)
            if(a.left):
                st.append([a.left,d+1])
            if(a.right):
                st.append([a.right,d+1])
        return ans