# https://leetcode.com/problems/partition-list/

# Основная идея - сохранять два отдельных списка, а потом сцепить их

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        # Всегда проверяй пустой случай
        if head is None:
            return head
        
        less_head, less_tail, more_head, more_tail = None, None, None, None
        current = head

        while True:
            if current.val < x:
                # надо прицепить к головному списку
                # а есть ли он?
                if less_head is None:
                    # потом надо будет вернуть указатель на голову
                    less_head = ListNode(current.val, None)
                    # хвост
                    less_tail = less_head
                # голова левого списка уже создана раньше
                else:
                    # значит "прицепим" хвост
                    less_tail.next = ListNode(current.val, None)
                    less_tail = less_tail.next
            else:
                if more_head is None:
                    more_head = ListNode(current.val, None)
                    more_tail = more_head
                else:
                    more_tail.next = ListNode(current.val, None)
                    more_tail = more_tail.next
            if current.next is None:
                break
            current = current.next
        
        if less_tail is None:
            return more_head
            
        less_tail.next = more_head
        return less_head

# testcases: [1], 2 
# testcases: [1], 0
# testcases: [1, 2, 3], 5
# testcases: [1, 2, 3], 0
# testcases: [4, 5, 6, 1], 2
