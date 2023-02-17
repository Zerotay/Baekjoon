n = int(input())
lst = [[0] * 10 for _ in range(100)]
for i in range(1, 10): lst[0][i] = 1
for i in range(1, n):
	for j in range(10):
		if not j : lst[i][j] = lst[i-1][1]
		elif j == 9: lst[i][j] = lst[i-1][8]
		else: lst[i][j] = lst[i-1][j-1] + lst[i-1][j+1]
print(sum(lst[n-1]) % 1000000000)

#해당 자리수에서 한 칸 뒤의 값이 뭐가 될 수 있는지를 나타낸다.