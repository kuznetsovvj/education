# https://codeforces.com/problemset/problem/785/A

d = {'Tetrahedron': 4 , 'Cube': 6, 'Octahedron': 8, 'Dodecahedron': 12, 'Icosahedron': 20}
t = int(input())
res = 0
for tt in range(t):
    l = input().strip()
    if l in d:
        res += d[l]
print(res)