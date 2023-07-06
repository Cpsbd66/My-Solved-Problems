problems = int(input())
ans = 0
for p in range(problems):
  A = list(map(int,input().split()))
  if(sum(A)>=2):
    ans += 1
print(ans)
