test = int(input())
for t in range(test):
    w = input()
    if(len(w)>10):
        n = str(len(w)-2)
        print(w[0]+n+w[len(w)-1])
    else:
        print(w)
