import sys
input = sys.stdin.readline

n = int(input())
inlst = [0] + [[*map(int, input().split())] for _ in range(n)]
lst = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(2, n+1):
	lst[i-1][i] = inlst[i-1][0] * inlst[i][0] * inlst[i][1]
for i in range(2, n+1):
	for j in range(1, n + 1 -i):
		lst[j][j+i] = 2 ** 32
		for k in range(j, j+i):
			lst[j][j+i] = min(lst[j][j+i], lst[j][k] + lst[k+1][j+i] + \
				inlst[j][0] * inlst[k][1] * inlst[j+i][1])
print(lst[1][n])

# N = int(input())
# matrix = []
# for _ in range(N):
#     matrix.append(list(map(int, input().split())))
# dp =[[0 for _ in range(N)] for _ in range(N)]


# for i in range(1, N): #몇 번째 대각선?
#     for j in range(0, N-i): #대각선에서 몇 번째 열?

#         if i == 1: #차이가 1밖에 나지 않는 칸
#             dp[j][j+i] = matrix[j][0] * matrix[j][1] * matrix[j+i][1]
#             continue

#         dp[j][j+i] = 2**32 #최댓값을 미리 넣어줌
#         for k in range(j, j+i):
#             dp[j][j+i] = min(dp[j][j+i],
#                              dp[j][k] + dp[k+1][j+i] + matrix[j][0] * matrix[k][1] * matrix[j+i][1])


# print(dp[0][N-1]) #맨 오른쪽 위