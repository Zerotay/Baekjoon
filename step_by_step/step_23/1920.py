n = int(input())
inlst = [*map(int, input().split())]
m = int(input())
iflst = [*map(int, input().split())]
inlst.sort()
for i in range(m):
	start = 0
	end = len(inlst) - 1
	while True:
		mid = (start + end) // 2
		if inlst[mid] < iflst[i]:
			start = mid + 1
		elif inlst[mid] > iflst[i]:
			end = mid - 1
		else:
			print(1)
			break
		if start > end:
			print(0)
			break
