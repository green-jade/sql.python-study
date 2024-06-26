N=int(input())

def dfs(x):
    visited[x]=1 # visited : 방문 체크 용 리스트, 방문시 1로 체크 
    node=arr[x]  # 현재 탐색 인덱스에 대한 value
    if visited[node]==0:
        dfs(node) 

for i in range(N):
    count=0
    T=int(input()) # 입력 숫자 개수

    visited=[0]*(T+1) # 방문 체크
    arr=[0] + list(map(int,input().split())) # 입력 어레이

    for i in range(1,T+1):
        if visited[i]==0:
            dfs(i)
            count+=1
    
    print(count)