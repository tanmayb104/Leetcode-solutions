# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if(not root):
            return []
        st=[[root,0]]
        l=[]
        s=0
        while(st):
            a,b=st.pop()
            if(b==s):
                l.append(a.val)
                s+=1
            if(a.left):
                st.append([a.left,b+1])
            if(a.right):
                st.append([a.right,b+1])
        return l