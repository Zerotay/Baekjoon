import sys

input = sys.stdin.readline
n, k = map(int, input().split())
inlst =  [0] * n
for i in range(n):
	inlst[i] = int(input())
answer = 0
for i in range(n-1, -1, -1):
	if inlst[i] <= k:
		answer += k // inlst[i]
		k %= inlst[i]
		if k == 0:
			break
print(answer)
