# https://codeforces.com/contest/1742/problem/F

from collections import defaultdict, Counter


def check(cmds):
    s, t = defaultdict(int), defaultdict(int)
    s['a'] = 1
    t['a'] = 1
    for cmd in cmds:
        c = Counter(cmd[2])
        for key in c.keys():
            if cmd[0] == 1:
                s[key] += c[key] * cmd[1]
            else:
                t[key] += c[key] * cmd[1]
        res = check_engine(s, t)
        if res:
            print("YES")
        else:
            print("NO")

def check_engine(s, t):
    s_keys = sorted(s.keys())
    t_keys = sorted(t.keys(), reverse=True)
    for i in range(len(s_keys)):
        # если в t буквы уже кончились, труба
        if len(t_keys) <= i:
            return False
        # если буква есть и в s, и в t, то сравниваем их
        if s_keys[i] < t_keys[i]:
            return True
        if s_keys[i] > t_keys[i]:
            return False
        # самая маленькая буква s равна самой большой букве t
        if s_keys[i] == t_keys[i]:
            if s[s_keys[i]] == t[t_keys[i]]:
                # одинаковых букв одинаково по числу
                if len(t_keys) == i + 1:
                    return False
                if len(s_keys) == i + 1:
                    return True
                continue
            if s[s_keys[i]] > t[t_keys[i]]:
                if len(t_keys) == i + 1:
                    return False
                return True
            if s[s_keys[i]] < t[t_keys[i]]:
                if len(s_keys) == i + 1:
                    return True
                return False



t = int(input())
for _ in range(t):
    tt = int(input())
    cmds = []
    for _ in range(tt):
        d, k, w = input().split()
        cmds.append((int(d), int(k), w))
    check(cmds)
