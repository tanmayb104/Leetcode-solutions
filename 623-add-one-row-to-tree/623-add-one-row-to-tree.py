# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if(depth==1):
            node=TreeNode(val)
            node.left=root
            return node
        else:
            d=2
            q=deque([root,-1])
            while(d!=depth):
                a=q.popleft()
                if(a==-1):
                    d+=1
                    if(len(q)):
                        q.append(-1)
                else:
                    if(a.left):
                        q.append(a.left)
                    if(a.right):
                        q.append(a.right)
            # print(q)
            for i in range(len(q)):
                if(q[i]!=-1):
                    a=q[i]
                    # print(a)
                    node=TreeNode(val)
                    temp=None
                    if(a.left):
                        temp=a.left
                    a.left=node
                    node.left=temp
                    node=TreeNode(val)
                    temp=None
                    if(a.right):
                        temp=a.right
                    a.right=node
                    node.right=temp
            return root
                    
            