test = int(input())
for t in range(test):
    n = int(input())
    lis = list(map(int,input().split()))
    mul = 1
    for i in lis:
        mul *= i
    k = 1
    current = lis[0]
    flag = True
    while(k<n):
        if(current == mul//current and mul%current ==0):
            print(k)
            flag = False
            break
        current *= lis[k]
        k += 1
        
    if(flag):print(-1)
