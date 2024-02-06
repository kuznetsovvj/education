# https://leetcode.com/problems/first-unique-character-in-a-string

def firstUniqChar(s):
    import collections
    c = collections.Counter(s)
    for idx, item in enumerate(s):
        if c[item] == 1:
            return idx
    return -1

assert firstUniqChar("leetcode") == 0
assert firstUniqChar("loveleetcode") == 2
assert firstUniqChar("aabb") == -1