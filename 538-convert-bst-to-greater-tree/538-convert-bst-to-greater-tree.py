# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from bisect import bisect
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         def rec(root):
#             nonlocal a
#             if(root.right):
#                 rec(root.right)
#                 root.val+=a
#                 a=root.val
#             else:
#                 root.val+=a
#                 a=root.val
#             if(root.left):
#                 root.val+=a
#                 a=root.val
#                 rec(root.left)
#             else:
#                 root.val+=a
#                 a=root.val
            
#         a=0
#         rec(root)
#         return root
        if(not root):
            return None
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
        t=[0 for i in range(len(l)+1)]
        for i in range(len(l)-1,-1,-1):
            t[i]=t[i+1]+l[i]
        # print(t)
        
        st=[root]
        while(st):
            a=st.pop()
            b=bisect_right(l,a.val)
            a.val=t[b-1]
            if(a.left):
                st.append(a.left)
            if(a.right):
                st.append(a.right)
        return root
            