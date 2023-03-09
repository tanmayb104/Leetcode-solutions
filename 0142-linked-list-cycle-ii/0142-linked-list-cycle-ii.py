# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow = head
        fast = head
        while(True):
            if(slow==slow.next):
                return slow
            if(fast and fast.next):
                fast=fast.next.next
                slow=slow.next
            else:
                return None
            if(fast==slow):
                break
        while(head!=slow):
            slow=slow.next
            head=head.next
        return head
        
        