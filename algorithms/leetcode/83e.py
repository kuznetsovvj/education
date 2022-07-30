# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # непонятно, могут ли передать изначально пустой список или нет?
        if head is None:
            return head

        previous = head
        current = head.next

        while current is not None:
            if current.val == previous.val:
                previous.next = current.next
            else:
                previous = current
            current = current.next
        
        return head