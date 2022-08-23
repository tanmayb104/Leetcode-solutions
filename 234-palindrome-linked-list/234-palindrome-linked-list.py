# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow,fast=head,head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        if fast:
            slow=slow.next
        temp=None
        prev=None
        while slow:
            temp=slow.next
            slow.next=prev
            prev=slow
            slow=temp
        slow=prev
        while(slow!=head and slow and head):
            if(slow.val!=head.val):
                return False
            slow=slow.next
            head=head.next
        return True