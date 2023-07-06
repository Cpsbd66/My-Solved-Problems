def solve():
    n = int(input())
    x = list(map(int, input().split()))
    likes = 0
    dislikes = 0
    for i in range(n):
        if x[i] > 0:
            likes += 1
        else:
            dislikes += 1
    
    for i in range(1, n + 1):
        if i <= likes:
            print(i, end=" ")
        else:
            print(likes * 2 - i, end=" ")
    print()

    for i in range(1, n + 1):
        if i <= dislikes * 2:
            print(i % 2, end=" ")
        else:
            print(i - dislikes * 2, end=" ")
    print()

test = int(input())
for t in range(test):
  solve()
