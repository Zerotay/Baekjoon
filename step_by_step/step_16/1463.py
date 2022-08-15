n = int(input())
if n == 1:
	print(0)
	exit(0)
elif n == 2:
	print(1)
	exit(0)

lst = [0 for _ in range(n + 1)]
lst[1] = 0
lst[2] = 1
lst[3] = 1
for i in range(3, n + 1):
	lst[i] = lst[i-1] + 1
	if i % 3 == 0:
		lst[i] = min(lst[i], lst[i//3] + 1)
	if i % 2 == 0:
		lst[i] = min(lst[i], lst[i//2] + 1)

print(lst[n])
