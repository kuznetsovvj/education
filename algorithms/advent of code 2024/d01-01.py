# https://adventofcode.com/2024/day/1

with open(r'input\01.txt', 'r') as file:
    s1, s2 = [], []
    res = 0
    for line in file.readlines():
        l1, l2 = list(map(int, line.strip().split('   ')))
        s1.append(l1)
        s2.append(l2)
    s1.sort()
    s2.sort()
    for i in range(len(s1)):
        res += abs(s1[i] - s2[i])
    print("Task1:", res)
    