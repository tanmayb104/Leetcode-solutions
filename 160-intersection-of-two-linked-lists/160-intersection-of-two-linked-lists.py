# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1=0
        h=headA
        while(h):
            l1+=1
            h=h.next
        l2=0
        h=headB
        while(h):
            l2+=1
            h=h.next
        if(l1>l2):
            p=l1-l2
            while(p):
                headA=headA.next
                p-=1
        else:
            p=l2-l1
            while(p):
                headB=headB.next
                p-=1
        while(headA and headB and headA!=headB):
            headA=headA.next
            headB=headB.next
        return headA