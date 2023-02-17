n = int(input())
p = 1000000007
mat = [[1,1],[1,0]]

def matmul(m1, m2):
	tmplst = [[0,0],[0,0]]
	for i in range(2):
		for j in range(2):
			e = 0
			for k in range(2):
				e += m1[i][k] * m2[k][j]
			tmplst[i][j] = e % p
	return tmplst

def square(m, k):
	if k == 1:
		for i in range(2):
			for j in range(2):
				m[i][j] %= p
		return m
	tmp = square(m, k//2)
	if k % 2:
		return matmul(matmul(tmp, tmp), mat)
	else:
		return matmul(tmp, tmp)

print(square(mat, n)[0][1])
