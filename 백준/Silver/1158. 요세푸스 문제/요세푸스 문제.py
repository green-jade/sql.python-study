n, k = map(int, input().split())
lst = list(range(1, n+1))

idx = 0
result = []

for i in range(n):
	idx = (idx+k-1) % len(lst)
	result.append(lst.pop(idx))
    
print('<' + str(result)[1:-1] + '>')