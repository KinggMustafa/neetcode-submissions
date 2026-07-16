# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        #we want right to start off at the start of the list + n
        while right and n:
            right = right.next
            n-= 1
        while right:
            left = left.next
            right = right.next
        #once right points to none, left will be exactly 1 + n from the end of our list so 1 node away from the node that needs to be rewritten
        left.next = left.next.next
        return dummy.next
        #o(n) time