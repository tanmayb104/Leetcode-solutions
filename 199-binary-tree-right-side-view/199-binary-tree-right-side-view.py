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
        q=collections.deque([root,-1])
        l=[]
        app=True
        while(q):
            a=q.popleft()
            if(app):
                l.append(a.val)
                app=False
            if(a==-1 and q):
                q.append(-1)
                app=True
            elif(a!=-1):
                if(a.right):
                    q.append(a.right)
                if(a.left):
                    q.append(a.left)
        return l