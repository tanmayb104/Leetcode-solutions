# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        c=0
        while(head and c<10**4+5):
            head=head.next
            c+=1
        if(head):
            return True
        return False
            