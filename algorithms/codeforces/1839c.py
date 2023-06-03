# https://codeforces.com/contest/1839/problem/C

# я не понял задание даже после наводящего вопроса - и решил какую-то другую задачу :)

def check(seq):
    res = []
    for i in range(len(seq)-1, -1, -1):
        if seq[i] != 0:
            print("NO")
            return
        else:
            if i > 0:
                if seq[i-1] == 0:
                    res.append(0)
                else:
                    res.append(i)
                    for j in range(i):
                        if seq[j] == 0:
                            seq[j] = 1
                        else:
                            seq[j] = 0
    res.append(0)
    print("YES")
    print(" ".join(map(str, res[::-1])))


for _ in range(int(input())):
    input()
    check(list(map(int, input().split())))