import sys

input = sys.stdin.readline
n = int(input())
lst = []
for _ in range(n):
	lst.append(list(map(int, input().split())))
for i in range(1, n):
	for j in range(i+1):
		if j > 0 and j < i:
			lst[i][j] += max(lst[i-1][j-1], lst[i-1][j])
		elif j > 0:
			lst[i][j] += lst[i-1][j-1]
		else:
			lst[i][j] += lst[i-1][j]
print(max(lst[n-1]))