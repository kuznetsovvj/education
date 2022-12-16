# https://codeforces.com/problemset/problem/580/C

# Типичный обход в глубину, но вершин много (10**5), поэтому надо сделать не на рекурсии, а на цикле

from collections import defaultdict


n, m = map(int, input().split())
seq = list(map(int, input().split()))
d = defaultdict(set)
for _ in range(n-1):
    a, b = map(int, input().split())
    d[a].add(b)
    d[b].add(a)
cur_cats = [0 for _ in range(n)] # последовательность котов на вершине - текущая
max_cats = [0 for _ in range(n)] # последовательность котов на вершине - максимальная

result = 0

st = [1]
cur_cats[0] = seq[0]
max_cats[0] = seq[0]

while st:
    current = st.pop()
    current_cat = cur_cats[current - 1]
    maxim_cat = max_cats[current - 1]
    if d[current]:
        for edge in d[current]:
            st.append(edge)
            d[edge].remove(current)
            if seq[edge - 1]:
                cur_cats[edge - 1] = current_cat + seq[edge - 1]
            else:
                cur_cats[edge - 1] = 0
            max_cats[edge - 1] = max(maxim_cat, cur_cats[edge - 1])
    else:
        if max_cats[current - 1] <= m:
            result += 1
    
print(result)  