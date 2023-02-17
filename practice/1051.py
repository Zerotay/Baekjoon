import sys
input = sys.stdin.readline

n, m = map(int, input().split())
inlst = [input().rstrip() for i in range(n)]

big = min(n, m)
ans = 0
while not ans:
	for i in range(0, n - big +1):
		for j in range(0, m-big +1):
			tmp = inlst[i][j]
			if inlst[i][j+big-1] != tmp: continue
			if inlst[i+big-1][j] != tmp: continue
			if inlst[i+big-1][j+big-1] != tmp: continue
			ans = big
	big -= 1

print(ans**2)