# https://leetcode.com/problems/minimum-time-to-make-rope-colorful

def minCost(colors, neededTime):
    res, crnt_clr, crnt_t = 0, colors[0], [neededTime[0]]
    for idx in range(1, len(colors)):
        if colors[idx] == crnt_clr:
            crnt_t.append(neededTime[idx])
        else:
            if len(crnt_t) > 1:
                res += sum(crnt_t) - max(crnt_t)
            crnt_t = [neededTime[idx]]
            crnt_clr = colors[idx]
    if len(crnt_t) > 1:
        res += sum(crnt_t) - max(crnt_t)
    return res

assert minCost("abaac", [1,2,3,4,5]) == 3
assert minCost("abc", [1,2,3]) == 0
assert minCost(colors = "aabaa", neededTime = [1,2,3,4,1]) == 2

