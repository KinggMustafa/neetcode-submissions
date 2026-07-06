# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0, None)
        curr = dummy
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0 
            val2 = l2.val if l2 else 0 
            total = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10
            curr.next = ListNode(total, None)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next
        return dummy.next
        #o(n) time where the longest n can be is the length of the longest list of nodes
        #o(n) space where n is the length of the longest list of nodes