# https://codeforces.com/problemset/problem/327/A

# С помощью обычного стека

def check(seq):
    cnt, stack, ones = 0, 0, 0
    for item in seq:
        if not stack:
            if item:
                cnt += 1
            else:
                stack += 1
        else:
            if item:
                ones += 1
                stack -= 1
            else:
                stack += 1
            if stack == 0:
                cnt += ones
                ones = 0
    return cnt

input()
seq = tuple(map(int, input().split()))
print(check(seq))
