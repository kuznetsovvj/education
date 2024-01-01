# https://leetcode.com/problems/largest-substring-between-two-equal-characters

def maxLengthBetweenEqualCharacters(s):
    d = {}
    for idx, item in enumerate(s):
        if item in d:
            d[item].append(idx)
        else:
            d[item] = list(idx)
    mx = -1
    for val in d.values():
        mx = max(mx, val[-1] - val[0] - 1)
    return mx

