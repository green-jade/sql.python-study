small=[]
for _ in range(9):
    height = int(input()) 
    small.append(height)
small.sort()

for i in range(9):
    for j in range(i+1,9):
        if sum(small) - small[i] - small[j] == 100:
            fake_1,fake_2=i,j
            continue
for idx in range(9):
    if idx == fake_1 or idx == fake_2:
        continue
    else:
        print(small[idx],'\n')