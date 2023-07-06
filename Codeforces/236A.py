word = input()

list1 = list(word)

list1 = list(set(list1))

n = len(list1)

if(n%2==0):
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
