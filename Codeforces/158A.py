c,k = map(int,input().split())
arr = list(map(int,input().split()))
minscore = arr[k-1]

ans = 0
for i in range(c):
    if(arr[i]>=minscore and arr[i]>0):
        ans += 1
print(ans)
