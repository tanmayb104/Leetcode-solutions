# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if(not head or not head.next):
            return head
        n=0
        temp=head
        while(temp):
            temp=temp.next
            n+=1
        k=k%n
        # print(k)
        if(k==0):
            return head
        end=head
        while(end.next):
            end=end.next
        p=n-k
        t=head
        prev=None
        while(p):
            # print(t.val)
            prev=t
            t=t.next
            p-=1
        prev.next=None
        end.next=head
        return t
        
        