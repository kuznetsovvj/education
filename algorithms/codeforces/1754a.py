# https://codeforces.com/problemset/problem/1754/A

def check(w):
    state = 0
    for i in range(len(w)):
        if w[i] == 'A':
            if state > 0:
                state -= 1
        else:
            state += 1
    if state > 0:
        return "No"
    return "Yes"
    

assert check("QA") == "Yes"
assert check("QAAQ") == "No"


t = int(input())
for _ in range(t):
    input()
    w = input()
    print(check(w))