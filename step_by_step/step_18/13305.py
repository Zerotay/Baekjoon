n = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))
dist.append(0)
price[-1] = 0
answer = 0
minimal = price[0]
val = 0
for i in range(n):
	if price[i] < minimal:
		answer += minimal * val
		minimal = price[i]
		val = dist[i]
	else:
		val += dist[i]
print(answer)
