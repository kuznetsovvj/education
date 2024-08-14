# https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds/description/

def numberOfChild(n, k):
    direction_right = ((k - 1) // (n - 1)) % 2 == 0
    step = k % (n-1)
    if step == 0:
        if direction_right:
            return n - 1
        else:
            return 0
    else:
        if direction_right:
            return step
        else:
            return n - 1 - step
        
assert numberOfChild(3, 5) == 1
assert numberOfChild(5, 6) == 2
assert numberOfChild(4, 2) == 2
assert numberOfChild(2, 1) == 1