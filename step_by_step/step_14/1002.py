import sys
import math

input = sys.stdin.readline

t = int(input())
for i in range(t):
	x1, y1, r1, x2, y2, r2 = map(int, input().split())
	if x1 == x2 and y1 == y2 and r1 == r2:
		print(-1)
		continue
	dt = math.hypot(x1 - x2, y1 - y2)
	if dt == float(r1 + r2) or max(r1, r2) == min(r1, r2) + dt:
		print(1)
	elif dt < float(r1 + r2) and max(r1, r2) < min(r1, r2) + dt:
		print(2)
	else:
		print(0)