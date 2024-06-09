from collections import deque
N,K = map(int,input().split())
deq = deque()
middle = N//2
for i in range(1,middle+1):
    if N % i == 0:
        deq.append(i)
    else:
        continue
deq.append(N)
if len(deq) >= K:
    print(deq[K-1])
else:
    print(0)