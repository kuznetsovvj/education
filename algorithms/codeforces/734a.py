# https://codeforces.com/problemset/problem/734/A

input()
a = input()
s = 0
for i in range(len(a)):
    if a[i] == 'A':
        s += 1
    else:
        s -= 1
if s > 0:
    print('Anton')
elif s < 0:
    print('Danik')
else:
    print('Friendship')