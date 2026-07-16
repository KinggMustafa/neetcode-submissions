# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        while head:
            if not head:
                return None
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        #list is now reversed, prev points to the new head
        position = 0
        curr = prev
        newhead = prev
        prev = ListNode(0)
        prev.next = curr
        while curr:
            position += 1
            nxt = curr.next
            if position == n:
                if newhead == curr:
                    newhead = nxt
                prev.next = nxt
                prev = curr
                curr.next = None
                curr = nxt
            else:
                prev.next = curr
                prev = curr
                curr = nxt
        prev = None
        while newhead:
            if not newhead:
                return None
    
            nxt = newhead.next
            newhead.next = prev
            prev = newhead
            newhead = nxt
        return prev

#O(n) time
            
                



