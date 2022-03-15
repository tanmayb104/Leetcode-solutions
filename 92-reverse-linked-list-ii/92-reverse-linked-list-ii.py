# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], l: int, r: int) -> Optional[ListNode]:
        if(not head.next):
            return head
        end=None
        trav=head
        prev=None
        a=1
        while(a!=l):
            prev=trav
            trav=trav.next
            a+=1
        start=trav
        start_prev=prev
        prev=trav
        trav=trav.next
        a+=1
        while(a!=r+1):
            temp=trav.next
            trav.next=prev
            prev=trav
            trav=temp
            a+=1
        start.next=trav
        if(start_prev):
            start_prev.next=prev
        else:
            head=prev
        return head
            
        
            
        