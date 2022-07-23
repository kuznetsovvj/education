# https://leetcode.com/problems/permutation-sequence/
# 60. Permutation Sequence

# Hard

def solution(n, k):
    import math
    items, res = [i + 1 for i in range(n)], []
    k = k - 1
    while n > 0:
        if n == 1:
            res.append(items[0])
        else:
            crt = k // math.factorial(n-1) 
            nxt = k - (crt * math.factorial(n-1))
            v = items[crt]
            res.append(v)
            k = nxt
            items.remove(v)
        n = n - 1
    return ''.join(map(str, res))


assert solution(1,1) == "1"
assert solution(2,1) == "12"
assert solution(2,2) == "21"


assert solution(3,1) == "123"
assert solution(3,2) == "132"
assert solution(3,3) == "213"
assert solution(3,4) == "231"
assert solution(3,5) == "312"
assert solution(3,6) == "321"

assert solution(4,9) == "2314"
