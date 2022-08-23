import sys
input = sys.stdin.readline

n, k = map(int, input().split())
inlst = [int(input()) for _ in range(n)]
start = 1
end = max(inlst)
while start <= end:
	mid = (start + end) // 2
	tmp = sum(map(lambda x: x//mid, inlst))
	if tmp < k:
		end = mid - 1
	else:
		start = mid + 1
print(end)
