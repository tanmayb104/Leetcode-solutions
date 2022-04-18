# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root):
        pass
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l=[]
        st=[root]
        while(st):
            a=st.pop()
            l.append(a.val)
            if(a.left):
                st.append(a.left)
            if(a.right):
                st.append(a.right)
        l.sort()
        return l[k-1]