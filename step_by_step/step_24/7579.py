import sys
input = sys.stdin.readline

n, m = map(int, input().split())
inlst1 = [*map(int, input().split())]
inlst2 = [*map(int, input().split())]

lst = [[0 for _ in range(sum(inlst2))] for _ in range(n)]
answer = sum(inlst2)
for i in range(n):
	for j in range(len(lst[0])):
		if inlst2[i] > j:
			lst[i][j] = lst[i-1][j]
		else:
			lst[i][j] = max(lst[i-1][j], inlst1[i] + lst[i-1][j-inlst2[i]])
		if lst[i][j] >= m:
			answer = min(answer, j)
print(answer)