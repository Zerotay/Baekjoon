n, b = map(int, input().split())
inlst = [list(map(int, input().split())) for _ in range(n)]

def simul(l1, l2):
	tmplst = [[0] * n for _ in range(n)]
	for i in range(n):
		for j in range(n):
			e = 0
			for k in range(n):
				e += l1[i][k] * l2[k][j]
			tmplst[i][j] = e % 1000
	return tmplst

def sqr(lst, k):
	if k == 1:
		for i in range(n):
			for j in range(n):
				lst[i][j] %= 1000
		return lst
	tmp = sqr(lst, k//2)
	if k % 2:
		return simul(simul(tmp, tmp), inlst)
	else:
		return simul(tmp, tmp)
for i in range(n):
	print(*sqr(inlst, b)[i])