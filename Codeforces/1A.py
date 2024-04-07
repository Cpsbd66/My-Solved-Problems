import math
 
n,m,a = map(int,input().split(" "))
row = math.ceil(n/a)
clmn = math.ceil(m/a)
print(row*clmn)
