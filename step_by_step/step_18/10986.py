n, m = map(int, input().split())
inlst = list(map(lambda x: int(x) % m, input().split()))
lst = [0] * m
tmp = 0
for i in range(n):
	tmp += inlst[i]
	lst[tmp % m] += 1
answer = lst[0]
for i in lst:
	answer += i * (i - 1) // 2
print(answer)