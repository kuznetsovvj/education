input()
w = input()

def check(w):
    cnt = {}

    for it in w:
        if it in cnt:
            cnt[it] += 1
        else:
            cnt[it] = 1

    # максимальная длина палиндрома - сама строка
    res = [0 for _ in range(len(w))]
    # номер последнего заполненного символа
    j = -1
    checked = False
    for k in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        # буква вообще есть
        if k in cnt:
            if not checked and cnt[k] % 2 == 1:
                checked = True
                mx_item = k
            if cnt[k] >= 2:
                for _ in range(cnt[k] // 2):
                    j += 1
                    res[j] = k
           
                   
    if checked:
        j += 1
        res[j] = mx_item

    s = 0
    if checked:
        ans = res[:j] + [res[j]] + res[:j][::-1]
    else:
        ans = res[:j+1] + res[:j+1][::-1]
   
    return ''.join(ans)
    

print(check(w))