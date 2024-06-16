# 유클리드 호제법
def gcd(x,y):
    x,y = max(x,y),min(x,y)
    while y > 0:
        x,y = y, x%y
    return x
def lcm(x,y):
    return x*y // gcd(x,y)

x,y=map(int,input().split())
print(gcd(x,y))
print(lcm(x,y))