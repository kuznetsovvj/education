# https://adventofcode.com/2023/day/2

def separate(round):
    col = round.split(',')
    res = {'blue': 0, 'green': 0, 'red': 0}
    for c in col:
        if c.find('blue') != -1:
            res['blue'] = int(c.strip()[:-5])
        if c.find('red') != -1:
            res['red'] = int(c.strip()[:-4])
        if c.find('green') != -1:
            res['green'] = int(c.strip()[:-6])
    return res


def check(line):
    game_num, colours = line.split(":")
    game_num = int(game_num[5:])
    rounds = colours.split(';')
    mx = {'blue': 0, 'green': 0, 'red': 0}
    for round in rounds:
        r = separate(round)
        for k in mx.keys():
            mx[k] = max(mx[k], r[k])

    if mx['blue'] <= 14 and mx['red'] <= 12 and mx['green'] <= 13:
        print(line, game_num, "TRUE")
        return game_num
    print(line, game_num, "FALSE")
    return 0


with open(r'C:\edu\algorithms\advent of code 2023\input\02.txt', 'r') as file:
    cnt = 0
    for line in file.readlines():
        cnt += check(line)
    
    print("Task1: ", cnt)

