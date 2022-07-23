#  https://codeforces.com/contest/1551/problem/C
#  сложность 1500


import sys

lyt = ('a', 'b', 'c', 'd', 'e')

def solution(words):
    res = []
    for word in words:
        res.append([word, {key: -len(word) for key in lyt}])
        for item in word:
            res[-1][1][item] += 2
    result = 0
    for value in lyt:
        cnt = 0
        i = 0
        for word in sorted(res, key=lambda x:x[1][value], reverse=True):
            cnt += word[1][value]
            if cnt > 0:
                i += 1
            result = max(i, result)
            if cnt < 0:
                break
    return result


inp = [line.strip() for line in sys.stdin]

i = 1
while i < len(inp):
    count = int(inp[i])
    words = tuple(inp[i + 1: i + count + 1])
    i = i + count + 1
    print(solution(words))

assert solution(["cbdca", "d", "a", "d", "e"]) == 3
assert solution(["bac", "aaada", "e"]) == 3
assert solution(["aba", "abcde", "aba"]) == 2
assert solution(["baba", "baba"]) == 0