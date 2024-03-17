input()
seq = tuple(map(int, input().split()))

res = 0
stack = [[seq[0], 1]]
for i in range(1, len(seq)):
    # шар есть и не поменялся
    if stack and stack[-1][0] == seq[i]:
        stack[-1][1] += 1
    # шара или нет, или он поменялся
    else:
        # шара нет
        if not stack:
            stack.append([seq[i], 1])
        # шар поменялся
        else:
            # если прошлых шаров больше трех - они сгорели
            if stack[-1][1] >= 3:
                res += stack[-1][1]
                stack.pop()
            # если шарик совпал - а он мог, после "сгорания"
            # то увеличиваем счетчик
            if stack[-1][0] == seq[i]:
                stack[-1][1] += 1
            else:
                stack.append([seq[i], 1])
if stack[-1][1] >= 3:
    res += stack[-1][1]
print(res)



        
    
