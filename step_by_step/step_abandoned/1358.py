import sys
import math
input = sys.stdin.readline

w, h, x, y, p = map(int, input().split())
r = h // 2
answer = 0
lst = [list(map(int, input().split())) for _ in range(p)]
for i in lst:
	if (x <= i[0] and i[0] <= x + w) and (y <= i[1] and i[1] <= y + h):
		answer += 1
	elif math.hypot(i[0] - x, i[1] - y - r) <= r:
		answer += 1
	elif math.hypot(i[0] - x - w, i[1] - y - r) <= r:
		answer += 1
print(answer)
