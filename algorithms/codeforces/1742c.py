# https://codeforces.com/contest/1742/problem/C

def check(matrix):
    for i in range(8):
        if matrix[i] == "R" * 8:
            return "R"
    return "B"


t = int(input())
for _ in range(t):
    input()
    matrix = []
    for _ in range(8):
        matrix.append(input())
    print(check(matrix))