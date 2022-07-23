# https://codeforces.com/problemset/problem/1535/A

def check(seq):
    if min(seq[0], seq[1]) > max(seq[2], seq[3]):
        return 'NO'
    
    if min(seq[2], seq[3]) > max(seq[0], seq[1]):
        return 'NO'
    
    return 'YES'

t = int(input())
for _ in range(t):
    print(check(tuple(map(int, input().split()))))