import sys
input = sys.stdin.readline

N = int(input())
stk = []

for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'push':
        stk.append(cmd[1])
    elif cmd[0] == 'pop':
        try:
            print(stk.pop())
        except IndexError:
            print(-1)
    elif cmd[0] == 'size':
        print(len(stk))
    elif cmd[0] == 'empty':
        print(int(len(stk)==0))
    elif cmd[0] == 'top':
        try:
            print(stk[-1])
        except IndexError:
            print(-1)