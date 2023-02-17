from bisect import bisect_left
n = int(input())
inlst = [*map(int, input().split())]
lst = [inlst[0]]
for i in inlst:
	if lst[-1] < i:
		lst.append(i)
	else:
		tmp = bisect_left(lst, i)
		lst[tmp] = i
print(len(lst))
