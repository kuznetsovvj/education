cmds, stack = input().split(), []

for cmd in cmds:
    if cmd in ('+', '-', '*'):
        v2 = stack.pop()
        v1 = stack.pop()
        if cmd == '+':
            stack.append(v1 + v2)
            continue
        if cmd == '-':
            stack.append(v1 - v2)
            continue
        if cmd == '*':
            stack.append(v1 * v2)
    else:
        stack.append(int(cmd))

print(stack.pop())

