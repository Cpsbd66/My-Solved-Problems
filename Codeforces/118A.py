s = input()
s = s.casefold()
vowels = ["A", "O", "Y", "E", "U", "I", "a", "e", "i", "o", "u", "y"]
base = []
for i in range(len(s)):
    if not((s[i] in vowels)):
        base.append(s[i])
n = len(base)
res = []
i = 0
while i<n:
    res.append(".")
    res.append(base[i])
    i += 1
result = "".join(res)
print(result)
