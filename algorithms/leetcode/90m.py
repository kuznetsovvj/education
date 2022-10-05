# https://leetcode.com/problems/subsets-ii/

# Простая задача (через itertools решать не спортивно)
# Сортировка в начале решает очень много проблем (без нее сложнее)

from copy import copy


def solution(nums):
    nums.sort()
    pos = [0 for _ in range(len(nums))]
    res = set()
    res.add(checker(nums, pos))
    while True:
        pos = next_pos(pos)
        if pos != -1:
            res.add(checker(nums, pos))
        else:
            break
    over = []
    for r in res:
        over.append(list(r))
    return over


def next_pos(pos):
    i = len(pos) - 1
    while i >= 0:
        if not pos[i]:
            pos[i] = 1
            for k in range(i+1, len(pos)):
                pos[k] = 0
            return pos
        i -= 1
    return -1
   

def checker(nums, pos):
    return tuple([num for (num, ps) in zip(nums, pos) if ps]) 
