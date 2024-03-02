n = int(input())
t = 1
l = [i+1 for i in range(n)]

for i in range(n):
    l[i], l[i // 2] = l[i // 2], l[i]

print(' '.join(map(str, l)))

