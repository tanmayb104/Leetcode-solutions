# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        a=head
        while(a):
            l.append(a.val)
            a=a.next
        l.sort()
        a=head
        for i in l:
            a.val=i
            a=a.next
        return head
                    
                    