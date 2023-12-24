# https://leetcode.com/problems/path-crossing/

def isPathCrossing(path):
    t = set()
    t.add((0, 0))
    c_x, c_y = 0, 0
    for i in path:
        if i == "N":
            c_y += 1
        if i == "S":
            c_y -= 1
        if i == "W":
            c_x -= 1
        if i == "E":
            c_x += 1
        if (c_x, c_y) in t:
            return True
        t.add((c_x, c_y))
    return False

assert isPathCrossing("NES") == False
assert isPathCrossing("NESWW") == True
    