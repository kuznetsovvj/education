# https://codeforces.com/contest/1841/problem/D
 
import sys
 
# исходное мое решение, которое валилось на 5-м тесте
def check(seq):
#    print(seq)
    seq.sort(key=lambda x:x[1])
    seq.sort(key=lambda x:x[0])
    res = 0
    x_fn = seq[0][1]
    first_mode = True
    for i in range(1, len(seq)):
        if first_mode:
            if seq[i][0] > x_fn:
                res += 1
                x_fn = seq[i][1]
            else:
                x_fn = max(seq[i][1], x_fn)
                first_mode = False
        else:
            if seq[i][0] > x_fn:
                x_fn = seq[i][1]
                first_mode = True
            else:
                x_fn = min(x_fn, seq[i][1])
                res += 1
    if first_mode:
        res += 1
    return res
 
# решение по идеям из editorial
def check2(seq):
    pairs = []
    # сформируем перечень всевозможных пар (т.е. пересечений двух отрезков), которые пересекаются
    for i in range(len(seq)):
        for j in range(i+1, len(seq)):
            if max(seq[i][0], seq[j][0]) <= min(seq[i][1], seq[j][1]):
                pairs.append((min(seq[i][0], seq[j][0]), max(seq[i][1], seq[j][1])))
    # сортируем по правой границе
    pairs.sort(key=lambda x:x[1])
    # подсчет количества
    cnt_pairs = 0
    last_pos = -1
    for item in pairs:
        if item[0] > last_pos:
            cnt_pairs += 1
            last_pos = item[1]
    if len(pairs) > 0:
        return len(seq) - 2 * cnt_pairs
    return len(seq)
 
 
input_ = [line.strip() for line in sys.stdin]
t = int(input_[0])
row = 1
for _ in range(t):
    cnt_row = int(input_[row])
    row += 1
    print(check2([tuple(map(int, line.split())) for line in input_[row:row+cnt_row]]))
    row += cnt_row