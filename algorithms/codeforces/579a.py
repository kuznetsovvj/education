# https://codeforces.com/problemset/problem/579/A

c = [1 for i in list(bin(int(input()))) if i == '1']
print(sum(c))