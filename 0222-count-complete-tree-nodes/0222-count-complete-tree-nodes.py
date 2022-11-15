# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if(not root):
            return 0
        st=[root]
        ans=1
        while(st):
            a=st.pop()
            if(a.left):
                st.append(a.left)
                ans+=1
            if(a.right):
                st.append(a.right)
                ans+=1
        return ans
                
        