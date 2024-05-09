T = int(input())

for _ in range(T):
    PS = list(input())
    stack = []
    VPS = True
    for i in PS:
        if i == "(":
            stack.append("(")
        else:
            try:
                stack.pop()
            except IndexError:
                VPS = False
                break
    
    if len(stack)==0 and VPS: 
        print("YES")
    else:
        print("NO")