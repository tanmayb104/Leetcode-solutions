# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self, head: ListNode):
        self.head = head # store head 
        
    def getRandom(self) -> int:
        node = self.head 
        n = 0
        while node: 
            if randint(0, n) == 0: ans = node.val
            n += 1
            node = node.next 
        return ans 
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()