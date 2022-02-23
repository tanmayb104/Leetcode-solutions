# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        flag=True
        if(not root):
            return []
        l=[[root.val]]
        q=deque([root,-1])
        t=[]
        while(q):
            a=q.popleft()
            if(a==-1 and len(q)):
                if(flag):
                    t=t[::-1]
                    l.append(t)
                else:
                    l.append(t)
                flag=not flag
                t=[]
                q.append(-1)
            elif(a!=-1):
                if(a.left):
                    q.append(a.left)
                    t.append(a.left.val)
                if(a.right):
                    q.append(a.right)
                    t.append(a.right.val)
        return l
            
        