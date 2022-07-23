# https://leetcode.com/problems/merge-intervals/
# 56. Intervals

# Medium

def solution(intervals):
    intervals.sort()
    res = [intervals[0]]
    for item in intervals[1:]:
        if item[0] <= res[-1][1]:
            res[-1][1] = max(item[1], res[-1][1])
        else:
            res.append(item)
    return res
    

assert solution([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
assert solution([[1,5],[2,7],[1,6]]) == [[1,7]]
