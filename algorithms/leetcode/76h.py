# https://leetcode.com/problems/minimum-window-substring/

import collections

def minWindow(s, t):

    def check(aim, cand):
        for k, v in aim.items():
            if cand[k] < v:
                return False
        return True

    # cd current dict, td - template dictionary
    cd, td = collections.defaultdict(int), collections.defaultdict(int)
    ans = []
    for item in t:
        td[item] += 1
    l, r = 0, 0
    cd[s[l]] += 1
    while r != len(s):
        if check(td, cd):
            # ответ найден
            ans.append((r-l+1, l, r))
            while check(td, cd):
                ans.append((r-l+1, l, r))
                if l == r:
                    break
                cd[s[l]] -= 1
                l += 1
            r += 1
            if r != len(s):
                cd[s[r]] += 1
        else:
            r += 1
            if r != len(s):
                cd[s[r]] += 1
    if len(ans) == 0:
        return ""
    mn = float('inf')
    m_l, m_r = 0, 0
    for mins, l, r in ans:
        if mins < mn:
            m_l, m_r = l, r
            mn = mins
    return s[m_l:m_r+1]

print(minWindow(s = "ADOBECODEBANC", t = "ABC"))
print(minWindow(s = "a", t = "a"))
print(minWindow(s = "a", t = "aa"))
print(minWindow(s = "ab", t = "b"))
