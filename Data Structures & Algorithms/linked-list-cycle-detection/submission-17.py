# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = head
        if not slow.next or not slow.next.next:
            return False
        fast = slow.next.next
        while fast != None and fast.next != None and fast.next.next != None:
            if slow == fast:
                return True
            else:
                slow = slow.next
                fast = fast.next.next
        return False