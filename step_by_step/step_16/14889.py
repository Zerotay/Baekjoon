from itertools import combinations

n = int(input())
lst = []
for _ in range(n):
	lst.append(list(map(int, input().split())))
startlink = [i for i in range(n)]
comb = list(combinations(startlink, n // 2))
start = list(comb[:len(comb) // 2])
link = list(reversed(comb[len(comb) // 2:]))
ans = 50000
for i in range(len(start)):
	sum_start = 0
	sum_link = 0
	for j in start[i]:
		for k in start[i]:
			sum_start += lst[j][k]
	for j in link[i]:
		for k in link[i]:
			sum_link += lst[j][k]
	diff = abs(sum_link - sum_start)
	if diff < ans:
		ans = diff
print(ans)