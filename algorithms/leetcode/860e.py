# https://leetcode.com/problems/lemonade-change/description/?envType=daily-question&envId=2024-08-15

def lemonadeChange(bills):
    i5, i10 = 0, 0
    for bill in bills:
        if bill == 5:
            i5 += 1
        if bill == 10:
            if i5 < 1:
                return False
            i5 -= 1
            i10 += 1
        if bill == 20:
            if i10 < 1:
                if i5 < 3:
                    return False
                i5 -= 3
            else:
                i10 -= 1
                if i5 < 1:
                    return False
                i5 -= 1
    return True