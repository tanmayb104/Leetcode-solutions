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
        q=deque([root,-1])
        ans=[]
        flag=True
        while(q):
            # print(q)
            a=q.popleft()
            if(a==-1):
                flag=True
                if(q):
                    q.append(-1)
            else:
                if(flag):
                    ans.append(a.val)
                    flag=False
                if(a.right):
                    q.append(a.right)
                if(a.left):
                    q.append(a.left)
        return ans
                