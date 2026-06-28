# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        setnodes = set()
        curr = head
        while curr:
            if curr in setnodes:
                return True
            else:
                setnodes.add(curr)
                curr = curr.next
        return False
        #o(n) time and space 
