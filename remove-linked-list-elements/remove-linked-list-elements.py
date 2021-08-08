# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while(head and head.val==val):
            head=head.next
        if(head):
            prev=head
            now=head.next
            while(now):
                if(now.val==val):
                    prev.next=now.next
                    now=now.next
                else:
                    prev=now
                    now=now.next
        return head