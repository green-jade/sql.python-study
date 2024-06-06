# 상근이가 가지고 있는 숫자 카드들
n = int(input())
list0 = list(map(int,input().split()))
# 포함여부를 판단해야 하는 숫자들
m = int(input())
list1 = list(map(int,input().split()))

dictionary = {}
for i in range(n):
    dictionary[list0[i]] = -1

# 출력
for i in list1:
    if i in dictionary:
        print(1, end=" ")
    else:
        print(0, end=" ")