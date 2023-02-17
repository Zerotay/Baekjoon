import sys
import heapq as hq
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
	val = int(input())
	valst = [abs(val), -1 if val < 0 else 1]
	if not val:
		if lst:
			tmp, ab = hq.heappop(lst)
			print(tmp * ab)
		else:
			print(0)
	else:
		hq.heappush(lst, valst)
