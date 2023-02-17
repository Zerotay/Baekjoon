import sys
input = sys.stdin.readline

x, y = map(int, input().split())
inlst = [[0 for _ in range(101)] for _ in range(101)]
inlst[x][y] = 1
for _ in range(int(input())):
	a, b = input().split()
	n = int(b)
	if a == 'R':
		while n:
			inlst[x][y] = 1
			y += 1
			n -= 1
	elif a == 'D':
		while n:
			inlst[x][y] = 1
			x += 1
			n -=1
	elif a == 'L':
		while n:
			inlst[x][y] = 1
			y -= 1
			n -= 1
	else:
		while n:
			inlst[x][y] = 1
			x -= 1
			n -= 1

def is_in(a, b):
	if -1 < a < 101 and -1 < b < 101:
		return True
	return False

def find_rt(a, b):
	if 0 < a < 100 and 1 < b < 101:
		if inlst[a+1][b] and inlst[a][b-1]:
			return True
	return False


def get_size(a, b):
	x, y = a, b
	flag = True
	while is_in(x,y):
		flag = False
		if not inlst[x][y]:
			break
		if inlst[x][y-1]:
			flag = True
			break
		x += 1
	if not flag:
		return 0
	y -= 1
	while is_in(x,y):
		flag = False
		if not inlst[x][y]:
			break
		if inlst[x-1][y]: #이려면 시작점부터 참조할 위험
			flag = True
			break
		y -= 1


ans = []
for i in range(1, 100):
	for j in range(1, 100):
		if inlst[i][j] == 1 and find_rt(i,j):
			tmp = get_size(i,j)
			ans.append(get_size(i,j))


for i in range(30):
	for j in range(30):
		print(inlst[i][j], end=' ')
	print()
# for i in range(30):
# 	for j in range(30):
# 		print((i,j) if inlst[i][j] else None)

if inlst[7][3]:
	print(1)
if inlst[10][5]:
	print(1)
