# https://codeforces.com/contest/1650/problem/A

def solution(w, c):
    if c not in w:
        return "NO"
    pos = 0
    while True:
        pos = w.find(c, pos)
        if pos == -1:
            break
        if (pos + 1) % 2 != 0:
            if len(w) == 3 and pos == 1:
                pos += 1
                continue
            return "YES"
        else:
            pos += 1
    return "NO"


k = int(input())
for i in range(k):
    w = input()
    c = input()
    print(solution(w, c))


assert solution("a", "b") == "NO"
assert solution("aba", "b") == "NO"
assert solution("abcde", "c") == "YES"
assert solution("abcde", "b") == "NO"
assert solution("abcdb", "b") == "YES"
assert solution("aaaaaaa", "a") == "YES"
assert solution("contest", "t") == "YES"