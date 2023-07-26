# https://codeforces.com/contest/1845/problem/A

def check(n, k, x):
    if x != 1:
        print("YES", n, ' '.join(['1' for _ in range(n)]), sep='\n')
        return
    # x = 1
    if k == 1:
        print("NO")
        return
    if n % 2 == 0:
        print("YES", n // 2, ' '.join(['2' for _ in range(n // 2)]), sep='\n')
        return
    else:
        if k < 3:
            print("NO")
            return
        print("YES", 1 + (n - 3) // 2, '3 ' + ' '.join(['2' for _ in range((n - 3) // 2)]), sep='\n')

for _ in range(int(input())):
    check(*map(int, input().split()))