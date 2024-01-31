input()
a = tuple(map(int, input().split()))
s = set(a)
a = list(s)
a.sort()

res = ""
state = False
state_st, state_fn = 0, 0
for i in range(len(a)):
    if not state:
        if i != len(a) - 1 and a[i] == a[i+1] - 1:
            state = True
            state_st = i
        else:
            res += str(a[i]) + " "
    else:
        if i != len(a) - 1 and a[i] == a[i+1] - 1:
            continue
        else:
            if i - state_st > 1:
                res += str(a[state_st]) + " ... " + str(a[i]) + " "
            else:
                res += str(a[state_st]) + " " + str(a[i]) + " "
            state = False
res.strip()
print(res)



