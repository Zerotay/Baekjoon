import sys
import heapq as hq
input = sys.stdin.readline

n = int(input())
biglst = []
smalllst = []
for _ in range(n):
	val = int(input())

	if len(smalllst) == len(biglst):
		hq.heappush(smalllst, -val)
	else:
		hq.heappush(biglst, val)
	if biglst and biglst[0] < -smalllst[0]:
		stmp = -hq.heappop(smalllst)
		btmp = hq.heappop(biglst)
		hq.heappush(biglst, stmp)
		hq.heappush(smalllst, -btmp)
	print(-smalllst[0])
