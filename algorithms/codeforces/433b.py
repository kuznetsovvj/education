# https://codeforces.com/problemset/problem/433/B

input() 
seq = list(map(int, input().split()))

p_s = [0 for _ in range(len(seq))]
sort_s = [0 for _ in range(len(seq))]
p_s[0] = seq[0]
for i in range(1, len(seq)):
    p_s[i] = p_s[i - 1] + seq[i]
seq.sort()
sort_s[0] = seq[0]
for i in range(1, len(seq)):
    sort_s[i] = sort_s[i - 1] + seq[i]

for _ in range(int(input())):
    t, l, r = map(int, input().split())
    if t == 1:
        if l == 1:
            print(p_s[r-1])
        else:
            print(p_s[r-1] - p_s[l-2])
    else:
        if l == 1:
            print(sort_s[r-1])
        else:
            print(sort_s[r-1] - sort_s[l-2])
