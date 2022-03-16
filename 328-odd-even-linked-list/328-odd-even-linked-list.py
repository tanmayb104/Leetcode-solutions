# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=1
        dummy1=ListNode()
        dummy2=ListNode()
        newhead=dummy1
        evhead=dummy2
        while(head):
            print(head.val,dummy1.val,dummy2.val)
            if(a%2==1):
                dummy1.next=head
                dummy1=dummy1.next
            else:
                dummy2.next=head
                dummy2=dummy2.next
            head=head.next
            a+=1
        dummy1.next=evhead.next
        dummy2.next=None
        return newhead.next
                