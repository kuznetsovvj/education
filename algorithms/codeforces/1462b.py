# https://codeforces.com/problemset/problem/1462/B

def check(w):

    template = "2020"
    current = 0
    i = 0
    start = True
    while 1:
        if w[i] == template[current]:
            i += 1
            current += 1
        else:
            if not start:
                return "NO"
            i = current - 4
            start = False


        if current == 4:
            return "YES"


for _ in range(int(input())):
    input()
    print(check(input()))