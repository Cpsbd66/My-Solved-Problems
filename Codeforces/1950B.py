

def solve():
  n = int(input())
  for i in range(n):
      t = 2
      first = "#"
      second = "."
      if i % 2 == 1:
          first = "."
          second = "#"
      while t > 0:
          for j in range(n):
              p = 2
              while p > 0:
                  if j % 2 == 0:
                      print(first, end="")
                  else:
                      print(second, end="")
                  p -= 1
          print()
          t -= 1

def main():
  t = int(input())
  while t > 0:
      solve()
      t -= 1

if __name__ == "__main__":
  main()
