import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000000)

n, m = map(int, input().split())
inlst = [[*map(int, input().split())] for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def make_two(x, y):
	inlst[x][y] = 2
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if -1 < nx < n and -1 < ny < m:
			if not inlst[nx][ny]: make_two(nx, ny)


make_two(0,0)#외곽에 해당한다면 다 2로 만들어버리기

ans = -1
flag = True
while flag:
	flag = False
	for i in range(n):
		for j in range(m):
			if inlst[i][j] == 1:
				flag = True
				count = 0
				for k in range(4):
					nx = i + dx[k]
					ny = j + dy[k]
					if -1 < nx < n and -1 < ny < m:
						if inlst[nx][ny] == 2: count += 1
				if count > 1: inlst[i][j] = 0
	for i in range(n):
		for j in range(m):
			if inlst[i][j] == 2:
				for k in range(4):
					nx = i + dx[k]
					ny = j + dy[k]
					if -1 < nx < n and -1 < ny < m:
						if not inlst[nx][ny]: make_two(nx, ny)
	ans += 1

print(ans)


# from collections import deque
# import sys
# input = sys.stdin.readline
# # 0 inside air
# # 1 cheese
# # 2 outside air
# board = []
# dx = [1,0,-1,0]
# dy = [0,1,0,-1]

# def bfs(Queue):
#     if not Queue:
#         return
#     cheese = []
#     visited = [[False for _ in range(m)] for _ in range(n)]
#     q = deque(Queue)
#     while q:
#         x, y = q.popleft()

#         board[x][y] = 2
#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]
#             if 0 <= nx < n and 0 <= ny < m:
#                 if board[nx][ny] == 0 and not visited[nx][ny]:
#                     q.append((nx, ny))
#                     visited[nx][ny] = True
#                 if board[nx][ny] == 1 and not visited[nx][ny]:
#                     cheese.append((nx, ny))
#                     visited[nx][ny] = True
#     return cheese

# def step(cheese):
#     any_cheese = False
#     Q = []
#     if not cheese:
#         return any_cheese, Q
#     for (x, y) in cheese:
#         air = 0
#         for i in range(4):
#             if board[x+dx[i]][y+dy[i]] == 2:
#                 air += 1
#         if air >= 2:
#             board[x][y] = 0
#             Q.append((x, y))
#     return True, Q

# n, m = map(int, input().split())
# for _ in range(n):
#     cur = list(map(int, input().split()))
#     board.append(cur)

# ans = 0
# Q = [(0, 0)]
# while True:
#     cheese = bfs(Q)
#     cheese_left, Q = step(cheese)
#     if cheese_left:
#         ans += 1
#     else:
#         break

# print(ans)