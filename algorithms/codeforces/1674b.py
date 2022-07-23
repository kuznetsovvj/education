import sys

def sol(word):
    if ord(word[1]) > ord(word[0]):
        k = 1
    else:
        k = 0
    return 25 * (ord(word[0]) - ord('a')) + ord(word[1]) - ord('a') - k + 1


p = [line.strip() for line in sys.stdin]

for i in range(1, len(p)):
    print(sol(p[i]))