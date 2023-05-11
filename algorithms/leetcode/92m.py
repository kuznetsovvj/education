# Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head, left, right):
        if left == right:
            return head
        current_idx = 1
        current_node = head
        last_before, first_after = None, None
        while current_idx != left:
            if current_idx == left - 1:
                last_before = current_node
            current_idx += 1
            current_node = current_node.next
        stack = []
        while current_idx <= right:
            stack.append(current_node)
            current_idx += 1
            current_node = current_node.next
        first_after = current_node

        current_node = last_before
        flag = False
        while len(stack):
            next_ = stack.pop()
            if current_node is not None:
                current_node.next = next_
            current_node = next_
            if left == 1 and not flag:
                head = current_node
                flag = True


        current_node.next = first_after
        
        return head