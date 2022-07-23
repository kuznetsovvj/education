# https://leetcode.com/problems/unique-paths/
# 62. Unique Paths

# Medium

def solution(m, n):
    import math
    return math.factorial(m+n-2) // (math.factorial(n-1) * math.factorial(m-1))

assert solution(3,2) == 3
assert solution(3,7) == 28

    
    