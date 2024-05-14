import sys
from sys import stdin

k = int(stdin.readline()) 
stack= []

for i in range (0, k) :
    temp = int(stdin.readline())    
    if temp != 0: 
        stack.append(temp)
    else : 
        stack.pop()

print(sum(stack))