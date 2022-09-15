from itertools import combinations as cb

n, c = map(int, input().split())
inlst = [*map(int, input().split())]

lst1 = inlst[:n//2]
lst2 = inlst[n//2:]

sumlst1 = []
sumlst2 = []

for i in range(len(lst1) + 1):
	tmp = cb(lst1, i)
	for j in tmp:
		sumlst1.append(sum(j))

for i in range(len(lst2) + 1):
	tmp = cb(lst2, i)
	for j in tmp:
		sumlst2.append(sum(j))

sumlst2.sort()
ans = 0
for i in sumlst1:
	if i > c:
		continue
	s, e = 0, len(sumlst2) - 1
	while s <= e:
		mid = (s + e) // 2
		if sumlst2[mid] + i > c:
			e = mid - 1
		else:
			s = mid + 1
	ans += e + 1

print(ans)