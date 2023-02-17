import sys

input = sys.stdin.readline
lst = []
n = int(input())
for _ in range(n):
	lst.append(list(map(int, input().split())))
min_sum = [[0, 0, 0] for _ in range(n)]
min_sum[0] = lst[0]
def dp(n):
	for i in range(1, n):
		min_sum[i][0] = min(min_sum[i-1][1],min_sum[i-1][2]) + lst[i][0]
		min_sum[i][1] = min(min_sum[i-1][0],min_sum[i-1][2]) + lst[i][1]
		min_sum[i][2] = min(min_sum[i-1][1],min_sum[i-1][0]) + lst[i][2]
	return min(min_sum[n-1])
print(dp(n))