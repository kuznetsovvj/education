# https://codeforces.com/problemset/problem/1638/C

import sys
from collections import deque

# O(n^2) сложность - не прошло по TL
def solution(seq):
    current_cmp = 0
    cmp = [-1 for _ in range(len(seq))] # номер компоненты связности
    for i in range(len(seq)):
        if cmp[i] == -1:
            tmp, current = [i], -1
            # если для данного элемента компонента связности не определена
            for j in range(i, len(seq)):
                if seq[j] < seq[i]:
                    if cmp[j] == -1:
                        tmp.append(j)
                    else:
                        current = cmp[j]
            if current == -1:
                current = current_cmp
                current_cmp += 1
            for idx in tmp:
                cmp[idx] = current
    return current_cmp

def checkstack(stack):
    if len(stack) >= 2:
        i1 = stack[-1]
        i2 = stack[-2]
        if i1[0] < i2[1]:
            stack.pop()
            stack.pop()
            stack.append([min(i1[0], i2[0]), max(i1[1], i2[1])])
            stack = checkstack(stack)
    return stack

# O(n) - через один проход и стек, валится на 54-ом тесте RUNTIME ERROR
# локально не воспроизвелось, аллокция 10 000 листов внутри листа?
def solution2(seq):
    stack = [[seq[0], seq[0]]]
    for i in range(1, len(seq)):
        if seq[i] < stack[-1][1]:
            stack[-1][0] = min(stack[-1][0], seq[i])
            stack[-1][1] = max(stack[-1][1], seq[i])
            stack = checkstack(stack)
        else:
            stack.append([seq[i], seq[i]])
    return len(stack)


class Vertex:
    def __init__(self, min_, max_):
        self.min_ = min_
        self.max_ = max_


# тот же алгоритм, но на деке и с типизированным объектом
def solution3(seq):
    
    deq = deque([Vertex(seq[0], seq[0])])
    for i in range(1, len(seq)):
        if seq[i] < deq[-1].max_:
            tmp = deq.pop()
            deq.extend([Vertex(min(tmp.min_, seq[i]), max(tmp.max_, seq[i]))])
            checkdeq(deq)
        else:
            deq.extend([Vertex(seq[i], seq[i])])
    return len(deq)

def checkdeq(deq):
    while len(deq) >= 2:
        if deq[-1].min_ < deq[-2].max_:
            i1 = deq.pop()
            i2 = deq.pop()
            deq.extend([Vertex(min(i1.min_, i2.min_), max(i1.max_, i2.max_))])
        else:
            return deq
    return deq


input_ = [list(map(int, line.strip().split())) for line in sys.stdin]

for i in range(2, len(input_), 2):
    print(solution3(input_[i]))