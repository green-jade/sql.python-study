# 내장함수 이용없이 재귀호출
def getBinaryNum(n, lists):
    div, mod = divmod(n, 2)
    lists.append(mod)
    if div == 0 :
        return lists
    else :
        return getBinaryNum(div, lists)

def getBinarylist(x):
    answerList = []
    answer = getBinaryNum(x,answerList)
    return sum(answer)

def solution(a, b):
    cnt=0
    for i in range(a,b+1):
        cnt += getBinarylist(i)
    return cnt

# 내장함수 bin()이용
def solution(a,b):
    return sum(bin(i)[2:] for i in range(a,b+1))