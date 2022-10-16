# https://codeforces.com/contest/1744/problem/B

def check(nums, cmd):
    c_sum, c_cnt = 0, 0
    nc_sum, nc_cnt = 0, 0
    for num in nums:
        if num % 2 == 0:
            c_sum += num
            c_cnt += 1
        else:
            nc_sum += num
            nc_cnt += 1
    for cm in cmd:
        if cm[0] == 0:
            # ко всем четным добавляем cm[1]
            if cm[1] % 2 == 0:
                # ко всем четным добавляем четное - получаем четные
                c_sum += cm[1] * c_cnt
            else:
                # ко всем четным добавляем нечетное - получаем нечетные
                nc_sum += cm[1] * c_cnt + c_sum
                c_sum = 0
                nc_cnt += c_cnt
                c_cnt = 0
        else:
            # ко всем нечетным добавляем cm[1]
            if cm[1] % 2 == 0:
                nc_sum += cm[1] * nc_cnt
            else:
                # к нечетным добавляем нечетное
                c_sum += cm[1] * nc_cnt + nc_sum
                nc_sum = 0
                c_cnt += nc_cnt
                nc_cnt = 0
        print(nc_sum + c_sum)
        

t = int(input())
for _ in range(t):
    _, k = tuple(map(int, input().split()))
    nums = tuple(map(int, input().split()))
    cmd = []
    for _ in range(k):
        cmd.append(tuple(map(int, input().split())))
    check(nums, cmd)