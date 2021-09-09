# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if(l1 and l2 and l1.val<=l2.val):
            now=l1
            l1=l1.next
        elif(l1 and l2 and l1.val>l2.val):
            now=l2
            l2=l2.next
        elif(not l1):
            return l2
        else:
            return l1
        head=now
        while(l1 and l2):
            if(l1.val<=l2.val):
                now.next=l1
                l1=l1.next
                now=now.next
            else:
                now.next=l2
                l2=l2.next
                now=now.next
        while(l1):
            now.next=l1
            l1=l1.next
            now=now.next
        while(l2):
            now.next=l2
            l2=l2.next
            now=now.next
        return head
                