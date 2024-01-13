# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram

from collections import defaultdict

def check(w):
    dc = defaultdict(int)
    for i in w:
        dc[i] += 1
    return dc

def minSteps(s: str, t: str) -> int:
    dc_s = check(s)
    dc_t = check(t)
    keys = set(dc_s.keys()).union(set(dc_t.keys()))
    to_insert, to_delete = 0, 0
    for key in keys:
        if dc_s[key] - dc_t[key] > 0:
            to_insert += dc_s[key] - dc_t[key]
        else:
            to_delete += dc_t[key] - dc_s[key]
    res = max(to_insert, to_delete)
    return res

assert minSteps(s = "leetcode", t = "practice") == 5

            
    