# https://adventofcode.com/2024/day/1
from collections import Counter


with open(r'input\01.txt', 'r') as file:
    s1, s2 = [], []
    res = 0
    for line in file.readlines():
        l1, l2 = list(map(int, line.strip().split('   ')))
        s1.append(l1)
        s2.append(l2)
    
    c = Counter(s2)
    for item in s1:
        res += item * c.get(item, 0)
    
    print("Task2:", res)
