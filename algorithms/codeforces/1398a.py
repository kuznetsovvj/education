# https://codeforces.com/problemset/problem/1398/A

def check(seq):
    if seq[0] + seq[1] <= seq[-1]:
        return f"1 2 {len(seq)}"
    return -1

for _ in range(int(input())):
    input()
    print(check(tuple(map(int, input().split()))))
