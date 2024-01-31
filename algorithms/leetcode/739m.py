# https://leetcode.com/problems/daily-temperatures/description

import bisect
import collections


def dailyTemperatures(temperatures):
    t = collections.deque([])
    res = [0 for _ in range(len(temperatures))]
    for idx, item in enumerate(temperatures):
        if not t:
            t.append((item, idx))
        else:
            i = bisect.bisect_left(t, item, key=lambda x:x[0])
            if i > 0:
                z = 0
                while z < i:
                    res[t[0][1]] = idx - t[0][1]
                    z += 1
                    t.popleft()
            t.appendleft((item, idx))

    return res

print(dailyTemperatures([73,74,75,71,69,72,76,73]))
print(dailyTemperatures([30,40,50,60]))
        
                

    
