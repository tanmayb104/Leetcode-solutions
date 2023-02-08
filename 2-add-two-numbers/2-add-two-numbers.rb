# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end

# @param {ListNode} l1
# @param {ListNode} l2
# @return {ListNode}
def add_two_numbers(l1, l2)
    dummy = ListNode.new(0)
    current = dummy
    carry = 0
    
    while l1 || l2 || carry != 0
        sum = carry
        if l1
            sum += l1.val
            l1 = l1.next
        end
        if l2
            sum += l2.val
            l2 = l2.next
        end
        
        carry = sum / 10
        sum = sum % 10
        current.next = ListNode.new(sum)
        current = current.next
    end
    
    dummy.next
end