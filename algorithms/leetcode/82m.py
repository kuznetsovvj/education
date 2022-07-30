# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def deleteDuplicates(self, head):

        from collections import defaultdict

        # непонятно, могут ли передать изначально пустой список или нет?
        if head is None:
            return head

        cnt = defaultdict(int)
        current = head
        while True:
            cnt[current.val] += 1
            current = current.next
            if current is None:
                break
        
        while cnt[head.val] != 1:
            head = head.next
            if head is None:
                return head
        
        if head is None:
            return head

        previous = head
        current = head.next
        while current is not None:
            if cnt[current.val] > 1:
                previous.next = current.next
            else:
                previous = current
            current = current.next
            

        return head


a = ListNode(val=1,next=None)
s = Solution()
s.deleteDuplicates(a)