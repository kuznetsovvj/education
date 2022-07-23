# https://codeforces.com/problemset/problem/705/A

n = int(input())
res = []
hate = True
while n > 0:
    if hate:
        res.append("I hate")
    else:
        res.append("I love")
    n -= 1
    hate = not hate
    if n >= 1:
        res.append("that")
    else:
        res.append("it")
print(' '.join(res))