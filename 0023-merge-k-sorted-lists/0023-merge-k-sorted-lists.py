# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if(not lists):
            return None    
        ans=ListNode(0)
        head=ans
        h=[]
        val=0
        for i in lists:
            if(i):
                heappush(h,tuple([i.val,val,i]))
                val+=1
        while(h):
            # print(h)
            a1,a2,a=heappop(h)
            ans.next=a
            if(a.next):
                heappush(h,tuple([a.next.val,val,a.next]))
                val+=1
                a.next=None
                ans=ans.next
            else:
                ans=ans.next
        return head.next
        
            
                    