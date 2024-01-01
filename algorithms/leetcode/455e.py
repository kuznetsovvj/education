# https://leetcode.com/problems/assign-cookies/

def findContentChildren(g, s):
    g.sort()
    s.sort()
    i_g, i_s = 0, 0
    res = 0
    while i_g < len(g) and i_s < len(s):
        if g[i_g] <= s[i_s] :
            res += 1
            i_g += 1
        i_s += 1
        
    return res

assert findContentChildren(g = [1,2,3], s=[1,1]) == 1
assert findContentChildren(g = [1,2], s = [1,2,3]) == 2
assert findContentChildren(g=[10,9,8,7], s=[5,6,7,8]) == 2
    