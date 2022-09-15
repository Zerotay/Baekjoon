def merge(a, p, q, r):
	global answer
	i, j, t = p, q+1, 1
	tmp = []
	while i <= q and j <= r:
		if a[i] <= a[j]:
			tmp.append(a[i])
			i += 1
		else:
			tmp.append(a[j])
			j += 1
	while i <= q:
		tmp.append(a[i])
		i += 1
	while j <= r:
		tmp.append(a[j])
		j += 1
	for i in range(len(tmp)):
		answer += 1
		if answer == k:
			print(tmp[i])
	i, t = p, 0
	while i <= r:
		a[i] = tmp[t]
		i += 1
		t += 1

def merge_sort(a, p, r):
	if p < r:
		q = (p+r) // 2
		merge_sort(a, p, q)
		merge_sort(a, q+1, r)
		merge(a, p, q, r)

n, k = map(int, input().split())
answer = 0
inlst = [*map(int, input().split())]
merge_sort(inlst, 0, len(inlst)-1)
if answer < k:
	print(-1)