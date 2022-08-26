import sys
import heapq as hq
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
	val = int(input())
	if not val:
		if lst:
			print(hq.heappop(lst))
		else:
			print(0)
	else:
		hq.heappush(lst, val)
