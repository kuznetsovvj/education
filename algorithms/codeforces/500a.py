# https://codeforces.com/problemset/problem/500/A

n, t = map(int, input().split())
seq = tuple(map(int, input().split()))

cnt = 1
while cnt < t:
    cnt += seq[cnt - 1]
    
if cnt == t:
    print("YES")
else:
    print("NO")