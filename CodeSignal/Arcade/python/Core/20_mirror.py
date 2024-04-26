def solution(a):
    binary = bin(a)[2:]
    mirror = 0
    for i in range(len(binary)):
        mirror += int(binary[i])*(2**i)
    return mirror


# 내장함수 int (이진법 to 십진법)
# def solution(a):
#    return int(bin(a)[2:][::-1],2)