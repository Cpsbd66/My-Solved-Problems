test = int(input())

for t in range(test):
    a,b = map(int,input().split())
    if(a+b>6):print("YES")
    else:print("NO")
