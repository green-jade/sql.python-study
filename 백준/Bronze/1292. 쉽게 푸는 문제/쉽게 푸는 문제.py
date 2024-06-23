a,b = map(int,input().split())

list = [0]
for i in range(46):
    for _ in range(i):
        list.append(i)

print(sum(list[a:b+1]))