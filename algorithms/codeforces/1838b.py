# https://codeforces.com/contest/1838/problem/B
 
def check(seq):
    t = len(seq)
    one, two, mx = -1, -1, -1
    for idx, item in enumerate(seq):
        if item == 1:
            one = idx
        if item == 2:
            two = idx
        if item == t:
            mx = idx
 
    if mx < one and mx < two:
        return f"{mx+1} {min(one,two)+1}"
 
    if mx > one and mx > two:
        return f"{mx+1} {max(one,two)+1}"
 
    return f"{one+1} {two+1}"
    
 
for _ in range(int(input())):
    input()
    print(check(tuple(map(int, input().split()))))