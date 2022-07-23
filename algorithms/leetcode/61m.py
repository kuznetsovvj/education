# https://leetcode.com/problems/rotate-list/
# 61. Rotate List

# Medium

def solution(head, k):
    if head is None:
        return head
    cnt = 1
    current = head
    while current.next is not None:
        current = current.next
        cnt += 1
    offset = k % cnt
    if offset == 0:
        return head
    previous_head = head
    t = head
    for _ in range(cnt - offset - 1):
        t = t.next
    head = t.next
    t.next = None
    crt = head
    while crt.next is not None:
        crt = crt.next
    crt.next = previous_head
    return head
    