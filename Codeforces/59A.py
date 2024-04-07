string = input()

upper = 0
lower = 0
up="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lo="abcdefghijklmnopqrstuvwxyz"

for i in string:
    if i in up:
        upper+=1
    elif i in lo:
        lower+=1
        
if(lower>=upper):
    print(string.casefold())
else:
    print(string.upper())
