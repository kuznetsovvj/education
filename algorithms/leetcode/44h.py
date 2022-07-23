# https://leetcode.com/problems/wildcard-matching/
# leetcode 44
# hard

# ACCEPTED


import sys


def solution(s, p):
    # без мемоизации не проходит timelimit
    mem = [[-1 for _ in range(len(p)+1)] for _ in range(len(s)+1)]

    def check(pos_w, pos_p):
        nonlocal max_w, max_p, s, p 
        if mem[pos_w][pos_p] != -1:
            return mem[pos_w][pos_p]

        if pos_p == max_p:
            mem[pos_w][pos_p] = pos_w == max_w
            return pos_w == max_w
        
        if p[pos_p] == '*':
            if pos_w == max_w:
                mem[pos_w][pos_p] = check(pos_w, pos_p + 1)
                return mem[pos_w][pos_p]
            else:
                mem[pos_w][pos_p] = check(pos_w, pos_p + 1) or check(pos_w + 1, pos_p + 1) or check(pos_w + 1, pos_p)
                return mem[pos_w][pos_p]
    
        else:
            if pos_w == max_w:
                mem[pos_w][pos_p] = False
                return False
            
            if p[pos_p] == '?':
                mem[pos_w][pos_p] = check(pos_w + 1, pos_p + 1)
                return mem[pos_w][pos_p]
            

            if p[pos_p] != s[pos_w]:
                mem[pos_w][pos_p] = False
                return False
            
            mem[pos_w][pos_p] = check(pos_w + 1, pos_p + 1)
            return mem[pos_w][pos_p]

    # возможно лишняя оптимизация с несколькими "*" подряд
    if len(p) != 0:
        np = p[0]
        for i in range(1, len(p)):
            if p[i] == '*' and np[-1] == '*':
                continue
            else:
                np += p[i]
    else:
        np = p
    p = np

    max_w, max_p = len(s), len(p)
    return check(0, 0)


assert solution("aa", "a") == False
assert solution("aa", "*") == True
assert solution("cb", "?a") == False
assert solution("adceb", "*a*b") == True
assert solution("acdcb", "a*c?b") == False