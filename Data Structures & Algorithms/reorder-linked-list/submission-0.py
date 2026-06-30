# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #first we have to get slow in the middle of the array
        slow = head
        fast = head
        while fast and fast.next:#we have to account for both even and an odd number of nodes
            slow = slow.next
            fast = fast.next.next
        curr = slow.next
        slow.next = None
        prev = None #sever the first half the list and set prev to none to reverse the second half
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        #now we must merge the two
        while head and prev:
            nxthead = head.next
            nxtprev = prev.next
            head.next = prev
            prev.next = nxthead
            head = nxthead
            prev = nxtprev

            
            