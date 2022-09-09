import sys
input = sys.stdin.readline
inf = int(1e9)

n, m = map(int, input().split())
inlst = [[*map(int, input().split())] for _ in range(m)]

lst = [inf] * (n+1)
lst[1] = 0
for i in range(n):
	for a,b,c in inlst:
		if lst[a] != inf and lst[b] > lst[a] + c:
			if i == n-1:
				print(-1)
				exit(0)
			lst[b] = lst[a] + c
print(*[i if i != inf else -1 for i in lst[2:]], sep='\n')