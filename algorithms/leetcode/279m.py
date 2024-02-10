# https://leetcode.com/problems/perfect-squares

import math

def numSquares(n):

    def check(n):
        s = math.sqrt(n)
        return int(s) == s
    
    if check(n):
        return 1
    
    # теорема Лагранжа о трех/четырех квадратах как есть
    while n % 4 == 0:
        n /= 4
    
    if (n % 8 == 7):
        return 4
    
    s = math.sqrt(n)
    for i in range(1, int(s) + 1):
        y = n - i * i
        if check(y):
            return 2
        
    return 3

assert numSquares(12) == 3
assert numSquares(13) == 2