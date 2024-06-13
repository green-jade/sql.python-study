people = 0
list = []
for i in range(10):
    a,b = map(int,input().split())
    people = people-a+b
    list.append(people)

print(max(list))