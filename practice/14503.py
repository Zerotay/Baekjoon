import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r,c,d = map(int, input().split())
inlst = [[*map(int, input().split())] for _ in range(n)]


dx = [-1,0,1,0]
dy = [0,1,0,-1]
# 북, 동, 남, 서
#dx

def chec(x, y):
	if not inlst[x][y]:
		return True
	return False

ans = 0
check = 0

inlst[r][c] = 2
while True:
	print(r,c,d)
	d -= 1
	if d < 0: d = 3

	if check == 4:
		d -= 2
		if d < 0: d = 3
		if inlst[r+dx[d]][c+dy[d]]==1:
			break
		else:
			check = 0
			r += dx[d]
			c += dy[d]
			#4번 도는 지 확인. 뒤있나.

	if d == 0:
		if chec(r+dx[d], c+dy[d]):
			r -= 1
			inlst[r][c] = 2
			check = 0
		else:
			pass
	elif d == 1:
		if chec(r+dx[d], c+dy[d]):
			c += 1
			inlst[r][c] = 2
			check = 0
		else:
			pass
		if chec(r+dx[d], c+dy[d]):
			r += 1
			inlst[r][c] = 2
			check = 0
		else:
			pass
		if chec(r+dx[d], c+dy[d]):
			c -= 1
			inlst[r][c] = 2
			check = 0
		else:
			pass

	check += 1

for i in inlst:
	for j in i:
		if j == 2:
			ans += 1
print(ans)

# print(*inlst, sep='\n')