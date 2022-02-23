# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        le=0
        h=head
        while(h):
            le+=1
            h=h.next
        le=le-n
        h=head
        if(le-1<0):
            return head.next
        while(le-1):
            h=h.next
            le-=1
        h.next=h.next.next
        return head