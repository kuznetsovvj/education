# https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal

def makeEqual(words):
    import collections
    t = collections.defaultdict(int)
    for word in words:
        for i in word:
            t[i] += 1
    for value in t.values():
        if value % len(words) != 0:
            return False
    return True

assert makeEqual(words = ["abc","aabc","bc"]) == True
assert makeEqual(words = ["ab", "a"]) == False
    
