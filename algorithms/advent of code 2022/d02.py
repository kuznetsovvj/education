# https://adventofcode.com/2022/day/2


line = r'input\02.txt'

with open(line, 'r') as file:
    cnt = 0
    games = {'X': {'v':1, 'A':'draw', 'B':'lose', 'C':'win'}, 
             'Y': {'v':2, 'A':'win', 'B':'draw', 'C':'lose'},
             'Z': {'v':3, 'A':'lose', 'B':'win', 'C':'draw'}}
    value = {'win':6, 'draw':3, 'lose':0}

    value3 = {'A':1, 'B':2, 'C':3}


    cnt2 = 0
    games2 = {'X': 'lose', 'Y': 'draw', 'Z': 'win'}
    values2 = {'win': {'A':'B', 'B':'C', 'C':'A'},
               'draw': {'A':'A', 'B':'B', 'C':'C'},
               'lose': {'A':'C', 'B':'A', 'C':'B'}}
    
    for line in file.readlines():
        a, b = line.strip().split()
        cnt += games[b]['v'] + value[games[b][a]]
        cnt2 += value[games2[b]] + value3[values2[games2[b]][a]]

    print("Task1:", cnt)
    print("Task2:", cnt2)