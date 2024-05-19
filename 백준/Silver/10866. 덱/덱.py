import sys
input = sys.stdin.readline
from collections import deque
deq = deque()
N = int(input())

for i in range(N):
    cmd = input().split()
    if cmd[0] == "push_front":
        deq.appendleft(int(cmd[1]))
    elif cmd[0] == "push_back":
        deq.append(int(cmd[1]))
    elif cmd[0] == "pop_front":
        try:
            print(deq.popleft())
        except IndexError:
            print(-1)
    elif cmd[0] == "pop_back":
        try:
            print(deq.pop())
        except IndexError:
            print(-1)

    elif cmd[0] == "size":
        print(len(deq))
    elif cmd[0] == "empty":
        print(int(len(deq)==0))

    elif cmd[0] == "front":
        try:
            print(deq[0])
        except IndexError:
            print(-1)
    else:
        try:
            print(deq[-1])
        except IndexError:
            print(-1)