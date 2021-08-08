# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head=ListNode()
        h=head
        while(l1 and l2):
            if(l1.val<l2.val):
                temp=ListNode(l1.val)
                head.next=temp
                head=head.next
                l1=l1.next
            else:
                temp=ListNode(l2.val)
                head.next=temp
                head=head.next
                l2=l2.next
        while(l1):
            temp=ListNode(l1.val)
            head.next=temp
            head=head.next
            l1=l1.next
        while(l2):
            temp=ListNode(l2.val)
            head.next=temp
            head=head.next
            l2=l2.next
        return h.next
                