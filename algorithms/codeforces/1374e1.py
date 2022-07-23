# https://codeforces.com/contest/1374/problem/E1
# Дорешивание

import sys
from collections import deque


reader = (tuple(map(int, line.split())) for line in sys.stdin)
both, alice, bob = [], [], []
n, k = next(reader)
for _ in range(n):
    value, alice_fl, bob_fl = next(reader)
    if alice_fl and bob_fl:
        both.append(value)
    if alice_fl and not bob_fl:
        alice.append(value)
    if not alice_fl and bob_fl:
        bob.append(value)
both.sort()
both = deque(both)
alice.sort()
alice = deque(alice)
bob.sort()
bob = deque(bob)
cnt_alice, cnt_bob = 0, 0
result = 0
while cnt_alice < k and cnt_bob < k:
    if len(both) > 0 and len(alice) > 0 and len(bob) > 0:
        if both[0] <= alice[0] + bob[0]:
            result += both.popleft()
        else:
            result += alice.popleft() + bob.popleft()
        cnt_alice += 1
        cnt_bob += 1
    else:
        if len(alice) == 0 or len(bob) == 0:
            if len(both) > 0:
                result += both.popleft()
                cnt_alice += 1
                cnt_bob += 1
            else:
                result = -1
                break
        else: # alice != 0 and bob != 0   =>  both = 0
            result += alice.popleft()
            result += bob.popleft()
            cnt_alice += 1
            cnt_bob += 1
print(result)



    






