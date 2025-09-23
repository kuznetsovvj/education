# https://leetcode.com/problems/furthest-building-you-can-reach/description

def furthestBuilding(heights, bricks, ladders):
    def check(deltas, bricks, ladder):
        for i in deltas:
            if i < bricks:
                bricks -= i
                continue
            else:
                if ladder > 0:
                    ladder -=1 
                else:
                    return False
        return True


    from bisect import insort_left
    deltas = []
    for i in range(1, len(heights)):
        d = heights[i] - heights[i-1]
        if d <= 0:
            continue
        insort_left(deltas, d)
        if not check(deltas, bricks, ladders):
            return i - 1
    return len(heights) - 1

def furthestBuilding2(heights, bricks, ladders):
    import heapq
    deltas = []
    for i in range(1, len(heights)):
        d = heights[i] - heights[i-1]
        if d <= 0:
            continue
        bricks -= d
        x = heapq.heappush(deltas, -d)
        if bricks < 0:
            b += -heapq.heappop(deltas)
            ladders -= 1
        if ladders < 0:
            return i - 1
        return len(heights) - 1



print(furthestBuilding2([4,2,7,6,9,14,12], 5, 1))
print(furthestBuilding2(heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2))
print(furthestBuilding2(heights = [14,3,19,3], bricks = 17, ladders = 0))


        