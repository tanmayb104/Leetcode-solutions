# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self,head1,head2):
        # print(head1,head2)
        head=self.head
        while(head1 and head2):
            if(head1.val<=head2.val):
                head.next=head1
                head=head.next
                head1=head1.next
            else:
                head.next=head2
                head=head.next
                head2=head2.next
        while(head1):
            head.next=head1
            head=head.next
            head1=head1.next
        while(head2):
            head.next=head2
            head=head.next
            head2=head2.next
        # print("111",self.head)
        return self.head.next
        
    def mergesort(self,head):
        if(not head.next):
            return head
        mid=head
        fast=head
        while(fast and fast.next):
            prev=mid
            mid=mid.next
            fast=fast.next.next
        prev.next=None
        h1=self.mergesort(head)
        h2=self.mergesort(mid)
        return self.merge(h1,h2)
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head):
            return None
        self.head=ListNode()
        return self.mergesort(head)            
                    