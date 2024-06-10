T = int(input())

def solution(x):
    binary = bin(x)[2:][::-1]
    for i in range(len(binary)):
        if binary[i] == '1':
            print(i,end=' ')

for i in range(T):
    num = int(input())
    solution(num)