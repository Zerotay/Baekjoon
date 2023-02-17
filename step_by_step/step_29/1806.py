n, s = map(int, input().split())
inlst = [*map(int, input().split())]
i1 = i2 = 0
tmp = inlst[0]
ans = set()
while i1 < n:
	if tmp < s:
		if i2 == n-1: break
		i2 += 1
		tmp += inlst[i2]
	else:
		ans.add(i2-i1+1)
		tmp -= inlst[i1]
		i1 += 1

print(min(ans) if ans else 0)