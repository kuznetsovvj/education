# https://codeforces.com/problemset/problem/711/A

fl = False
res = []
for _ in range(int(input())):
    line = input()
    if fl:
        res.append(line)
    else:
        if line[0:2] == 'OO':
            res.append(f"++{line[2:]}")
            fl = True
        elif line[3:] == 'OO':
            res.append(f"{line[:3]}++")
            fl = True
        else:
            res.append(line)

if fl:
    print("YES")
    for item in res:
        print(item)
else:
    print("NO")

