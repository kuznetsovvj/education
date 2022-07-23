def minDistance(word1, word2):
    mtx = [[float('inf') for _ in range(len(word1) + 1)] for _ in range(len(word2) + 1)]
    mtx[0][0] = 0
    for j in range(1, len(word1) + 1):
        mtx[0][j] = mtx[0][j-1] + 1
    for i in range(1, len(word2) + 1):
        mtx[i][0] = mtx[i-1][0] + 1
        for j in range(1, len(word1) + 1):
            if word1[j-1] != word2[i-1]:
                mtx[i][j] = min(mtx[i-1][j], mtx[i][j-1], mtx[i-1][j-1]) + 1
            else:
                mtx[i][j] = mtx[i-1][j-1]
    return mtx[-1][-1]

print(minDistance("horse", "ros"))

assert minDistance("horse", "ros") == 3
assert minDistance("intention", "execution") == 5 