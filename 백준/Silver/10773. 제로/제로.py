import sys
k = int(sys.stdin.readline())

stk = []

for _ in range(k):
    number = int(sys.stdin.readline()) 
    if number != 0:
        stk.append(number)
    else:
        if stk: 
            stk.pop()

print(sum(stk))
