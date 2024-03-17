from collections import deque

deq = deque()
pos = {}
out = 0

for _ in range(int(input())):
    cmd = input()
    if cmd[0] == '1':
        id = int(cmd[2:])
        pos[id] = len(deq) + out
        deq.append(id)
        continue
    if cmd[0] == '2':
        deq.popleft()
        out += 1
        continue
    if cmd[0] == '3':
        deq.pop()
        continue
    if cmd[0] == '4':
        id = int(cmd[2:])
        print(pos[id] - out)
    if cmd[0] == '5':
        print(deq[0])
        
    

    