# https://adventofcode.com/2023/day/1

with open(r'input\01.txt', 'r') as file:
    cnt = 0
    for line in file.readlines():
        for i in line:
            if i.isdigit():
                cnt += int(i) * 10
                break
        for i in line[::-1]:
            if i.isdigit():
                cnt += int(i)
                break

    print("Task1:", cnt)
    