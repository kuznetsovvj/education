# https://adventofcode.com/2022/day/1

with open(r'input\01.txt', 'r') as file:
    elfs = []
    cnt = 0
    for line in file.readlines():
        if line != '\n':
            cnt += int(line)
        else:
            elfs.append(cnt)
            cnt = 0
    elfs.append(cnt)
    elfs.sort(reverse=True)

    print("Task1:", elfs[0])
    print("Task2:", sum(elfs[:3]))