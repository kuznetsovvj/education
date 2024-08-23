# https://leetcode.com/problems/fraction-addition-and-subtraction/description/?envType=daily-question&envId=2024-08-23

import math


def fractionAddition(expression):
    state = 'sign'
    current_numerator = 0
    current_denominator = 0
    value_numerator = 0S
    value_denominator = 1
    for i in expression:
        if state == 'sign':
            if i == '-':
                negativeSign = True
            else:
                if i != '+':
                    current_numerator = current_numerator * 10 + int(i)
                negativeSign = False
            state = 'numerator'
        elif state == 'numerator':
            if i.isdigit():
                current_numerator = current_numerator * 10 + int(i)
            else:
                state = 'denominator'
        elif state == 'denominator':
            if i.isdigit():
                current_denominator = current_denominator * 10 + int(i)
            else:
                if negativeSign:
                    negativeSign = -1
                else:
                    negativeSign = 1
                new_value_denominator = value_denominator * current_denominator
                new_value_numerator = value_numerator * current_denominator + negativeSign * current_numerator * value_denominator
                value_denominator = new_value_denominator
                value_numerator = new_value_numerator
                current_denominator = 0
                current_numerator = 0
                if i == '-':
                    negativeSign = True
                else:
                    negativeSign = False
                state = 'numerator'
    
    if negativeSign:
        negativeSign = -1
    else:
        negativeSign = 1
    new_value_denominator = value_denominator * current_denominator
    new_value_numerator = value_numerator * current_denominator + negativeSign * current_numerator * value_denominator
    value_denominator = new_value_denominator
    value_numerator = new_value_numerator

    gcd = math.gcd(value_denominator, value_numerator)
    if gcd > 1:
        value_numerator = value_numerator // gcd
        value_denominator = value_denominator // gcd

    return f"{value_numerator}/{value_denominator}"
                

#assert fractionAddition("-1/2+1/2") == "0/1"
#assert fractionAddition("-1/2+1/2+1/3") == "1/3"
assert fractionAddition("1/3-1/2") == "-1/6"

    
