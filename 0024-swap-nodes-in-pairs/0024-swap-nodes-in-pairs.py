class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        a=1
        prev=head
        now=head.next
        while(prev and now and now!=prev):
            # print(prev.val,now.val)
            if(a==1):
                new_head=now
                temp=now.next
                now.next=prev
                prev.next=temp
                new_ne=prev
                now,prev=prev,now
            elif(a%2==1):
                temp=now.next
                now.next=prev
                prev.next=temp
                new_ne.next=now
                new_ne=prev
                now,prev=prev,now
            prev=prev.next
            now=now.next
            a+=1
        return new_head