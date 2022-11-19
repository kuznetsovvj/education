# https://codeforces.com/problemset/problem/451/B

def check(seq):
    # массив из одного элемента всегда отсортирован
    if len(seq) == 1:
        print('yes')
        print('1 1')
        return
    
    st, fn = -1, -1
    for i in range(1, len(seq)):
        if seq[i] < seq[i-1]:
            st = i - 1
            break
    
    for i in range(len(seq)-1,0,-1):
        if seq[i] < seq[i-1]:
            fn = i
            break
    
    if st == -1 and fn == -1:
        print('yes')
        print('1 1')
        return

    seq = seq[0:st] + tuple(reversed(seq[st:fn+1])) + seq[fn+1:]

    for i in range(1, len(seq)):
        if seq[i] < seq[i-1]:
            print('no')
            return

    print('yes')
    print(f'{st+1} {fn+1}')


input()
seq = tuple(map(int, input().split()))
check(seq)

