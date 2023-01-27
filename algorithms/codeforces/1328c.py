# https://codeforces.com/problemset/problem/1328/C

def check(x):
    f1 = True
    mx, mn = ['1'], ['1']
    for i in x[1:]:
        if i == '0':
            mx.append('0')
            mn.append('0')
            continue
        if i == '1':
            if f1:
                mx.append('1')
                mn.append('0')
                f1 = False
            else:
                mx.append('0')
                mn.append('1')
            continue
        if i == '2':
            if f1:
                mx.append('1')
                mn.append('1')
            else:
                mx.append('0')
                mn.append('2')
    print(''.join(mx))
    print(''.join(mn))

for _ in range(int(input())):
    input()
    check(input())
    