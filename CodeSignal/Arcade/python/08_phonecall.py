# phone usage rate에 따른 duration of the longest call(minutes rounded down to the nearest integer)구하기

def solution(min1, min2_10, min11, s):
    if s<=min1:
        return s//min1
    elif s<=min1+min2_10*9:
        return 1+(s-min1)//min2_10
    else:
        return 1+9+(s-min1-min2_10*9)//min11

