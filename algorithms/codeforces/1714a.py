# https://codeforces.com/contest/1714/problem/A

def check(current, times):
    times.sort()
    for time in times:
        if current < time:
            return check_different(current, time)
        if current == time:
            return "0 0"
    return check_more(current, times[0])


def check_different(current, time):
    delta = time - current
    return f"{delta // 60} {delta % 60}"

def check_more(current, time):
    delta = time + (1440 - current)
    return f"{delta // 60} {delta % 60}"

t = int(input())
for _ in range(t):
    k, hour, minute = map(int, input().split())
    current = hour * 60 + minute
    times = []
    for _ in range(k):
        hours, minutes = tuple(map(int, input().split()))
        times.append(hours * 60 + minutes)
    print(check(current, times))