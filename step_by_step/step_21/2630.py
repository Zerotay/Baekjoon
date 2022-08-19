blue, white = 0, 0

def dc(x,y,num):
	global blue, white
	tmp = inlst[x][y]
	for i in range(x, x+num):
		for j in range(y, y+num):
			if inlst[i][j] != tmp:
				dc(x, y, num//2)
				dc(x + num//2, y, num//2)
				dc(x , y + num//2, num//2)
				dc(x + num//2, y + num//2, num//2)
				return
	if tmp == '1':
		blue += 1
	else:
		white +=1

n = int(input())
inlst = [list(input().split()) for _ in range(n)]
dc(0,0,n)
print(white)
print(blue)