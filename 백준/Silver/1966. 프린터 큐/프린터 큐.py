# test case 갯수
T = int(input())
from collections import deque
for _ in range(T):
    N, M = map(int, input().split())         # N : 문서의 갯수 , M : 몇번째 문서?
    queue = deque(map(int, input().split())) # 중요도 나열 덱

    imp = max(queue)
    count = 0
    while queue:
        imp = max(queue)  
        front = queue.popleft() 
        M-= 1 

        if imp==front: 
            count += 1 
            if M < 0: 
                print(count)
                break

        else:  
            queue.append(front) 
            if M < 0 :  
                M = len(queue) - 1 