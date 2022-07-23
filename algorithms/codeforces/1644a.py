# https://codeforces.com/problemset/problem/1644/A

import sys
import string


def solution(s):
    k = {'r': False, 'b': False, 'g': False}
    for i in s:
        if i.isupper():
            if not k[i.lower()]:
                return 'NO'
        else:
            k[i] = True
    return 'YES'

input_ = [line.strip() for line in sys.stdin]
for pos in range(1, len(input_)):
    print(solution(input_[pos]))