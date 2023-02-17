n = int(input())
k = int(input())

s, e = 0, k
while s <= e:
	mid = (s + e) // 2
	if sum([min(mid//i, n) for i in range(1, n+1)]) < k: s = mid + 1
	else: e = mid - 1
print(s)