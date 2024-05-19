import sys
n = int(sys.stdin.readline())

stk = []
ans = []
status = True
num = 1
for _ in range(n):
    a = int(sys.stdin.readline())
    while num<= a:
        stk.append(num)
        ans.append('+')
        num += 1
    if stk[-1] == a:
        stk.pop()
        ans.append('-')
    else:
        status = False
        
if not status:
    print('NO')
else:
    for x in ans:
        print(x)