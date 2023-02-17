n = int(input())
inlst = sorted(map(int, input().split()), key=lambda x: abs(x))
dist = abs(inlst[0] + inlst[1])
ans = [inlst[0], inlst[1]]
for i in range(n-1):
	tmp = abs(inlst[i] + inlst[i+1])
	if tmp < dist:
		dist = tmp
		ans = inlst[i:i+2]

print(*sorted(ans))