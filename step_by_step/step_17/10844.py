n = int(input())

lst = [[0]*10 for _ in range(101)]
for i in range(1, 10):
	lst[1][i] = 1
for i in range(2, n+1):
	for j in range(10):
		if j == 0:
			lst[i][j] = lst[i-1][1]
		elif j == 9:
			lst[i][j] = lst[i-1][8]
		else:
			lst[i][j] = lst[i-1][j-1] + lst[i-1][j+1]
print(sum(lst[n]) % 1000000000)
