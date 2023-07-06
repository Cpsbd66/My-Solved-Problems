Test = int(input())
for t in range(Test):
	a, b, c = map(int, input().split(' '))
	if(c>=a and c<b):
	    print("YES")
	else:
	    print("NO")
