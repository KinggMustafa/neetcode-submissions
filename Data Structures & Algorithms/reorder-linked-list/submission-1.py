# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #first we have slow and fast, fast moves twice as fast, and slow will become the first half of the list of nodes
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #there is a difference between an even and odd amount of nodes
        #for [2,4,6,8] slow would be 6
        #for [2,4,6,8,10], slow would be 6
        #we want the bigger half of the array to not be the half we reverse
        curr = slow.next
        slow.next = None
        prev = None
        #now we reverse the second half of the array
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr 
            curr = nxt
        #now we merge the two lists of nodes
    #2,4,6
    #8,10
        reorder = head
        while reorder and prev:
            nxt = reorder.next
            reorder.next = prev
            prevnxt = prev.next
            prev.next = nxt
            prev = prevnxt
            reorder = nxt
        #o(n) time and constant space where n is the length of nodes
            