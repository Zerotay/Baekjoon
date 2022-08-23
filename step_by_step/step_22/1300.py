n = int(input())
k = int(input())
start = 1
end = n ** 2
while start <= end:
	mid = (start + end) // 2
	tmp = 0
	for i in range(1, n+1):
		tmp += min(mid//i, n)
	if tmp < k:
		start = mid + 1
	else:
		end = mid - 1
print(start)
