input()
l = list(map(int, input().split()))

def merge(left, right):
    res = []
    cnt = 0
    l_idx, r_idx = 0, 0
    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] < right[r_idx]:
            res.append(left[l_idx])
            l_idx += 1
        else:
            res.append(right[r_idx])
            r_idx += 1
            cnt += len(left) - l_idx
    while r_idx != len(right):
        res.append(right[r_idx])
        r_idx += 1
    while l_idx != len(left):
        res.append(left[l_idx])
        l_idx += 1
    return res, cnt
    

def cnt(l):
    if len(l) <= 1:
        return l, 0
    l_l = l[:len(l) // 2]
    l_r = l[len(l) // 2:]
    l_l, l_cnt = cnt(l_l)
    l_r, r_cnt = cnt(l_r)
    res, s_cnt = merge(l_l, l_r)
    return res, s_cnt + l_cnt + r_cnt

res, s_cnt = cnt(l)
print(s_cnt, ' '.join(map(str, res)), sep='\n')
    