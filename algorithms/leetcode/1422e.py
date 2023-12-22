# https://leetcode.com/problems/maximum-score-after-splitting-a-string/

def maxScore(s):
    c_l = s[0] == "0"
    c_r = sum([1 for i in range(len(s)-1) if s[i+1] == '1'])
    max_v = c_l + c_r
    for i in range(1, len(s) - 1):
        if s[i] == '0':
            c_l += 1
        else:
            c_r -= 1
        max_v = max(max_v, c_l + c_r)
    return max_v

assert maxScore("011101") == 5
assert maxScore("00111") == 5
assert maxScore("1111") == 3