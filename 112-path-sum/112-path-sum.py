# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right 
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if(not root):
            return False
        st=[[root,targetSum]]
        while(st):
            a,d=st.pop()
            if(not a.right and not a.left and d-a.val==0):
                return True
            if(a.right):
                st.append([a.right,d-a.val])
            if(a.left):
                st.append([a.left,d-a.val])
        return False
        
        
        