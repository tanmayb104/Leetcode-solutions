"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if(not root):
            return 
        q=collections.deque([root,-1])
        prev=root
        start=True
        while(q):
            a=q.popleft()
            if(a==-1 and len(q)):
                prev.next=None
                q.append(-1)
                start=True
            elif(a!=-1):
                if(a.left):
                    q.append(a.left)
                if(a.right):
                    q.append(a.right)
                if(start):
                    prev=a
                    start=False
                else:
                    prev.next=a
                    prev=a
        return root