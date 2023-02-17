s = input()
result = []
l = len(s)
for i in range(l + 1):
	for j in range(l - i):
		result.append(s[j : j + 1 + i])
print(len(set(result)))