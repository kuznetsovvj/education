# https://adventofcode.com/2023/day/1

d = {'two': 2, 'seven':7, 'nine':9, 'one':1, 'three':3, 'four':4,
     'five':5, 'six':6, 'eight':8 }

def early(word):

    for idx, item in enumerate(word):
        for k, v in d.items():
            if word.find(k) == idx:
                return v

def lastly(word):
    for idx in range(len(word), -1, -1):
        for k, v in d.items():
            if word.find(k) == idx:
                return v
            
def check(line):
    i = 0
    while not line[i].isdigit():
        i += 1
    if early(line[:i]):
        t = early(line[:i]) * 10
    else:
        t = int(line[i]) * 10
    
    j = len(line) - 1
    while not line[j].isdigit():
        j -= 1
    if lastly(line[j+1:]):
        p = lastly(line[j+1:])
    else:
        p = int(line[j])
    print(line, t + p)
    return t + p

assert check('2ninehnsnnvj21fkeightwodmz') == 22
assert check('drdhjjtdrdxonenineninefourfkzrrggvz97') == 17


with open(r'C:\edu\algorithms\advent of code 2023\input\01.txt', 'r') as file:
    cnt = 0
    for line in file.readlines():
        cnt += check(line)
    
    print("Task2: ", cnt)

