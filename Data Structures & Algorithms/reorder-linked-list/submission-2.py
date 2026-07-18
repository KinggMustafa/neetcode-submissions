# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        cut = head
        position = 0
        start = None
        while cut:
            position += 1
            if position == (length // 2) + 1:
                start = cut.next
                cut.next = None
            cut = cut.next
        #now we reverse the other half
        half = None
        while start:
            nxt = start.next
            start.next = half
            half = start
            start = nxt
        #half is now the start of the second half of the reversed linked list
        #head holds the first half

        dummy = ListNode(0, head)
        while head and half:
            nxt = head.next
            head.next = half
            nxthalf = half.next
            half.next = nxt
            head = nxt
            half = nxthalf
        #o(n) time and constant space
        


        
        



            

        