# 시간(분)을 hh:mm으로 나타냈을 때 4개의 각 숫자들을 더하는 함수

def solution(n):
    hour = n // 60
    min = n % 60
    return hour//10 + hour%10 + min//10 + min%10 

# 함수 map : map(function, iterable1, iterable2, ...)
def solution(n):
    return sum(map(int,str(n//60)+str(n%60)))

solution(808)