import sys

input = sys.stdin.readline
n = int(input())
inlst = []
inlst = [list(map(int, input().split())) for _ in range(n)]
inlst.sort(key=lambda x: (x[1], x[0]))
answer = 0
k = 0
for i in inlst:
	if k <= i[0]:
		k = i[1]
		answer += 1
print(answer)