# https://codeforces.com/contest/1650/problem/E


import sys


def solution(n, seq):
    # нулевой день экзамена
    seq = [0] + seq

    # найдем минимальную разницу между экзаменами и позицию
    min_, min_pos = n, 0
    for idx in range(1, len(seq)):
        if seq[idx] - seq[idx - 1] - 1 < min_:
            min_ = seq[idx] - seq[idx - 1] - 1
            min_pos = idx
    
    # новое расписание - все экзамены, кроме самого меньшего
    schedule = []
    for i in range(len(seq)):
        if i != min_pos:
            schedule.append(seq[i])


    res = count(schedule)
    if (min_pos > 1):
        schedule[min_pos - 1] = seq[min_pos]
    res = max(res, count(schedule))
    return res


def count(seq):
    max_, min_ = 0, float('inf')
    for idx in range(1, len(seq)):
        min_ = min(min_, seq[idx] - seq[idx - 1] - 1)
        max_ = max(max_, seq[idx] - seq[idx - 1] - 1)
    return min(min_, max(n - seq[-1] - 1, (max_ - 1) // 2))


input_ = [list(map(int, line.strip().split())) for line in sys.stdin]
for pos in range(2, len(input_), 3):
    _, n = input_[pos]
    seq = input_[pos + 1]
    print(solution(n, seq))