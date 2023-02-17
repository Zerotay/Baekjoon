import sys
input = sys.stdin.readline

n, c = map(int, input().split())
inlst = sorted([int(input()) for _ in range(n)])
start, end = 1, inlst[-1] - inlst[0]
while start <= end:
	mid = (start + end) // 2
	count = 1
	tmp = 0
	for i in range(1, n):
		if inlst[i] - inlst[tmp] >= mid:
			count += 1
			tmp = i
	if count < c:
		end = mid - 1
	else:
		start = mid + 1
print(end)
