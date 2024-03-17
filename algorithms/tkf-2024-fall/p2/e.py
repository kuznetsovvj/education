input()

seq = list(map(int, input().split()))
n = len(seq)
stack = []
# номер вагона, который мы сейчас ищем
i = 1
# порядковый номер вагона, который еще не заехал в тупик
k = 0
res = []

while True:
    # на вершине стека лежит нужный вагон
    if len(stack) != 0 and stack[-1] == i:
        res.append("2 1")
        stack.pop()
        i += 1
        if i > n:
            break
    else:
        if k == n:
            res = []
            break
        stack.append(seq[k])
        res.append("1 1")        
        k += 1
if len(res) == 0:
    print(0)
else:
    print(len(res))
    for item in res:
        print(item)

        
    
    

