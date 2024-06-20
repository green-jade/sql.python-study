N = int(input())
for i in range(N):
    lis = list(map(int,input().split()))
    lis.sort()
    print(lis[-3])