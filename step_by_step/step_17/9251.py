n = list(input())
m = list(input())
lst = [0] * len(n)
for i in range(len(m)):
	tmp = 0
	for j in range(len(n)):
		if tmp < lst[j]:
			tmp = lst[j]
		elif m[i] == n[j]:
			lst[j] = tmp + 1
print(max(lst))