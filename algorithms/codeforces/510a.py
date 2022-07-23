# https://codeforces.com/problemset/problem/510/A

x, y = map(int, input().split())
for t in range(x):
    if t % 2 == 0:
        print('#'*y)
    elif t % 4 == 1:
        print('.'*(y-1)+'#')
    else:
        print('#'+'.'*(y-1))