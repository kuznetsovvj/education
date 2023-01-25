# https://codeforces.com/problemset/problem/320/A

def check(w):
    # state machine
    # st = 0 // допускается только 1 (уже было две четверки или первая цифра)
    # st = 1 // была 1 (допускается 4 или 1)
    # st = 2 // была 4 (допускается 4 - но последняя или 1)
    st = 0
    for i in w:
        if st == 0:
            if i == '1':
                st = 1
                continue
            return "NO"
        if st == 1:
            if i == '1':
                st = 1
                continue
            if i == '4':
                st = 2
                continue
            return "NO"
        if st == 2:
            if i == '1':
                st = 1
                continue
            if i == '4':
                st = 0
                continue
            return "NO"
    return "YES"

print(check(input()))