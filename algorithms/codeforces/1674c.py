import sys
from collections import Counter

def sol(word, word2):
    if word2 == 'a':
        return 1
    c = Counter(word2)
    if c['a'] > 0:
        return -1
    d = Counter(word)
    return 2**d['a']    
    

p = [line.strip() for line in sys.stdin]

for i in range(1, len(p), 2):
    print(sol(p[i], p[i+1]))