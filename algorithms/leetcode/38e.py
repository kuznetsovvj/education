# https://leetcode.com/problems/count-and-say/
# leetcode 38
# easy

def countAndSay(n):
    current = None
    for _ in range(n):
        current = say(current)
    return current


def say(n):
    if n is None:
        return "1"
    else:
        res, crnt, amt = "", n[0], 1
        for item in n[1:]:
            if item == crnt:
                amt += 1
            else:
                res += f"{amt}{crnt}"
                crnt, amt = item, 1
        res += f"{amt}{crnt}"
        return res
