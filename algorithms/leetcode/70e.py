# https://leetcode.com/problems/climbing-stairs

def climbStairs(self, n: int) -> int:
    if n == 1:
        return 1
    res = [0 for _ in range(n)]
    res[0], res[1] = 1, 1
    for i in range(n):
        if i <= n-2:
            res[i+1] += res[i]
        if i <= n-3:
            res[i+2] += res[i]
    return res[n-1]  

assert climbStairs(2) == 2
assert climbStairs(3) == 3