# https://leetcode.com/problems/power-of-two

def isPowerOfTwo(n):
    return n > 0 and n & (n - 1) == 0

