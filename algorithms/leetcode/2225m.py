# https://leetcode.com/problems/find-players-with-zero-or-one-losses

def findWinners(matches):
    winners, losers, manylosers = set(), set(), set()
    for win, los in matches:
        # проверяем победителя
        if win not in manylosers and win not in losers:
            winners.add(win)
        # проверяем проигравшего
        if los in winners:
            winners.remove(los)
        if los not in losers:
            if los not in manylosers:
                # еще не проигрывал, но вот проиграл
                losers.add(los)
        else:
            losers.remove(los)
            manylosers.add(los)
    a = list(winners)
    a.sort()
    b = list(losers)
    b.sort()
    return [a, b]

print(findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))
print(findWinners([[2,3],[1,3],[5,4],[6,4]]))

            
        
