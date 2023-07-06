def check_pi(n, pi):
    count = 0
    for i in range(len(n)):
        if n[i] == pi[i]:
            count += 1
        else:
            break
    return count

t = int(input())
pi = "314159265358979323846264338327950288419716939937510"
for i in range(t):
    n = input()
    print(check_pi(n, pi))
