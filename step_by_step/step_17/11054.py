n = int(input())
lst = list(map(int, input().split()))
dp1 = [0] * n
dp2 = [0] * n
for i in range(n):
	for j in range(i):
		if lst[i] > lst[j] and dp1[i] < dp1[j]:
			dp1[i] = dp1[j]
	dp1[i] += 1
for i in range(n-1, -1, -1):
	for j in range(n-1, i-1, -1):
		if lst[i] > lst[j] and dp2[i] < dp2[j]:
			dp2[i] = dp2[j]
	dp2[i] += 1
ll = list(map(lambda x: x[0]+ x[1] - 1, list(zip(dp1, dp2))))
print(max(ll))