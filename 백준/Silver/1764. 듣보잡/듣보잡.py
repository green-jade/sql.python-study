import sys
input = sys.stdin.readline
N, M = map(int, input().split())

dict_1 = dict()
answer = []
for i in range(N):
    x = input()
    if x not in dict_1:
        dict_1[x] = i

for i in range(M):
    y = input()
    if y in dict_1:
        answer.append(y)
        
answer.sort()
print(len(answer))
print(''.join(answer), end = '')