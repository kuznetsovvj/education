# https://adventofcode.com/2023/day/4

def check(line):
    p1, p2 = line.split('|')
    _, p1 = p1.split(':')
    nums1 = set(map(int, p1.split()))
    nums2 = set(map(int, p2.split()))
    r = nums1.intersection(nums2)
    if len(r) == 0:
        return 0
    else:
        return 2 ** (len(r) - 1)

with open(r'C:\edu\algorithms\advent of code 2023\input\04.txt', 'r') as file:
    s = [1 for _ in range(1, 202)]
    i = 1
    for line in file.readlines():
        p1, p2 = line.split('|')
        _, p1 = p1.split(':')
        nums1 = set(map(int, p1.split()))
        nums2 = set(map(int, p2.split()))
        r = nums1.intersection(nums2)
        for t in range(1, len(r) + 1):
            s[i + t - 1] += s[i - 1] 
        i += 1

    print(sum(s))