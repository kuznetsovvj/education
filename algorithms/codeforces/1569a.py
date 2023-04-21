# https://codeforces.com/problemset/problem/1569/A
 
def check(w):
    if len(w) == 1:
        return "-1 -1"
    for i in range(1, len(w)):
        a = (w[i] == 'a') or (w[i-1] == 'a')
        b = (w[i] == 'b') or (w[i-1] == 'b') 
        if a and b:
            return f"{i} {i+1}"
    return "-1 -1"
 
for _ in range(int(input())):
    input()
    print(check(input()))