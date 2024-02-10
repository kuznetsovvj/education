# https://leetcode.com/problems/sort-characters-by-frequency

def frequencySort(s):
    from collections import defaultdict
    d = defaultdict(int)
    for item in s:
        d[item] += 1
    k = list(d.items())
    k.sort(key=lambda x:x[1], reverse=True)
    res = []
    for it, cnt in k:
        res.append(it*cnt)
    return ''.join(res)


print(frequencySort("c34dfaaabbcc"))

    
    
