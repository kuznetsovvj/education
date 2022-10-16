# https://codeforces.com/contest/1744/problem/D

def check(nums):
    aim = len(nums)
    cnt = 0
    res = 0
    for item in nums:
        while item % 2 == 0 and item > 0:
            cnt += 1
            item = item // 2
    if aim <= cnt:
        return res
    m = []
    for t in range(len(nums), -1, -1):
        cur_tmp = 0
        if t % 2 == 1:
            continue
        while t % 2 == 0 and t > 0:
            cur_tmp += 1
            t = t // 2
        m.append(cur_tmp)
    m.sort(reverse=True)
    for item in m:
        res += 1
        cnt += item
        if aim <= cnt:
            return res
    return -1

t = int(input())
for _ in range(t):
    input()
    nums = tuple(map(int, input().split()))
    print(check(nums))