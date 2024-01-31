input()
a = tuple(map(int, input().split()))
mn = min(a)
s = 0
for i in range(1, len(a)):
    s += (min(a[i], a[i-1]) - mn) + 0.5 * (abs(a[i] - a[i-1]))
print(s / (len(a) - 1) + mn)