# https://codeforces.com/contest/1840/problem/E
 
import sys
from collections import deque
 
 
def check(w1, w2, blocks, cmds):
    times = deque() # очередь для блокировки/разблокировки
    wrongs = 0 # количество несовпадающих символов
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            wrongs += 1
    for idx, cmd in enumerate(cmds):
        cmd = tuple(map(int, cmd.split()))
        if cmd[0] == 1:
            if w1[cmd[1]-1] != w2[cmd[1]-1]:
                wrongs -= 1
                times.append(idx + blocks)
        elif cmd[0] == 2:
            t1 = (w1[cmd[2]-1] != w2[cmd[2]-1]) + (w1[cmd[4]-1] != w2[cmd[4]-1])
            if cmd[1] == 1:
                a = w1
            else:
                a = w2
            if cmd[3] == 1:
                b = w1
            else:
                b = w2
            a[cmd[2]-1], b[cmd[4]-1] = b[cmd[4]-1], a[cmd[2]-1]
            t2 = (w1[cmd[2]-1] != w2[cmd[2]-1]) + (w1[cmd[4]-1] != w2[cmd[4]-1])
            if t1 != t2:
                wrongs = wrongs - t1 + t2
            
        elif cmd[0] == 3:
            while len(times) > 0:
                b = times.popleft()
                if b < idx + 1:
                    wrongs += 1
                else:
                    times.appendleft(b)
                    break
            if wrongs == 0:
                print("YES")
            else:
                print("NO")
 
    
input_ = [line.strip() for line in sys.stdin]
v = int(input_[0])
i = 1
for _ in range(v):
    w1 = input_[i]
    i += 1
    w2 = input_[i]
    i += 1
    b, rows = map(int, input_[i].split())
    i += 1
    cmds = input_[i:i+rows]
    i += rows
    check(list(w1), list(w2), b, cmds)