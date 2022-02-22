# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h=0
        len1=0
        len2=0
        h1=l1
        while(h1):
            h1=h1.next
            len1+=1
        h1=l2
        while(h1):
            h1=h1.next
            len2+=1
        if(len1>=len2):
            h1=l1
            h2=l2
            s=l1
        else:
            h1=l2
            h2=l1
            s=l2
        h=0
        while(h1.next and h2.next):
            h1.val+=h2.val+h
            h=h1.val//10
            h1.val=h1.val%10
            h1=h1.next
            h2=h2.next
        h1.val+=h2.val
        while(h1.next):
            h1.val+=h
            h=h1.val//10
            h1.val=h1.val%10
            h1=h1.next
        h1.val+=h
        h=h1.val//10
        h1.val=h1.val%10
        if(h):
            new = ListNode(h,None)
            h1.next=new
        return s
            