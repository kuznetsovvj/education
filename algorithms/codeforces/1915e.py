# https://codeforces.com/contest/1915/problem/E

# никакого удовольствия, сначала сделал на set() - не проходило по скорости

def check(seq):
    prev = [0]
    for i in range(len(seq)):
        if i % 2 == 1:
            j = prev[-1] - seq[i]
        else:
            j = prev[-1] + seq[i]       
        prev.append(j)
        if j == 0:
            return "YES"
    prev.sort()
    for i in range(1, len(prev)):
        if prev[i] == prev[i-1]:
            return "YES"
    return "NO"

for _ in range(int(input())):
    input()
    print(check(tuple(map(int, input().split()))))
               