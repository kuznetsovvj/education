def solution(sequence):
    stack = 0
    cnt = 0
    for item in sequence:
        if item == '(':
            stack += 1
        else:
            stack -= 1
            if stack < 0:
                cnt += 1
                stack = 0
    print(cnt)
 
 
inp = int(input())
for _ in range(inp):
    input()
    solution(input())