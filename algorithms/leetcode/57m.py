# https://leetcode.com/problems/insert-interval/
# 57. Insert Intervals

# Medium

def solution(intervals, newInterval):
    intervals.append(newInterval)
    intervals.sort()
    res = [intervals[0]]
    for item in intervals[1:]:
        if item[0] <= res[-1][1]:
            res[-1][1] = max(item[1], res[-1][1])
        else:
            res.append(item)
    return res
    

assert solution([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]
assert solution([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1,2],[3,10],[12,16]]
assert solution([], [5,7]) == [[5,7]]
assert solution([[1,5]], [2,3]) == [[1,5]]
assert solution([[1,5]], [2,7]) == [[1,7]]
