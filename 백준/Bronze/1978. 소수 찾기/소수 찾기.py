count=0
N = int(input())
nums = list(map(int,input().split()))

for num in nums:
    i=2
    while i<=int(num/2):
        if num%i==0: # 약수가 존재
            break
        else: # 나눠떨어지지 않음 
            i+=1
    if i ==int(num/2)+1:
        count+=1

print(count)