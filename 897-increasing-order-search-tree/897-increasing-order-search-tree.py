# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
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
        head=TreeNode(l[0])
        root=head
        for i in range(1,len(l)):
            root.right=TreeNode(l[i])
            root=root.right
        return head
        