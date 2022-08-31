import sys
input = sys.stdin.readline

def recur(num, weight):
	if num > n:
		return
	if dp[num][weight]:
		return
	dp[num][weight] = 1
	recur(num+1, weight)
	recur(num+1, weight + inlst[num-1])
	recur(num+1, abs(weight - inlst[num-1]))


n = int(input())
inlst = [*map(int, input().split())]
k = int(input())
tlst = [*map(int, input().split())]
dp = [[0 for _ in range(15501)] for _ in range(n+1)]

recur(0,0)
for i in tlst:
	print("Y" if dp[n][i] == 1 else "N", end=' ')

0

#이게 왜 안 되는지 잘 모르겠다
# import sys
# input = sys.stdin.readline

# n = int(input())
# inlst = [*map(int, input().split())]
# k = int(input())
# tlst = [*map(int, input().split())]
# setlst = [inlst[0], -inlst[0]]
# for i in range(1, n):
# 	for j in range(len(setlst)):
# 		setlst.append(setlst[j] + inlst[i])
# 		setlst.append(setlst[j] - inlst[i])
# 		# print(setlst)
# 	setlst = list(set(setlst))
# # print(setlst)
# for i in range(k):
# 	print('Y' if tlst[i] in setlst else 'N', end=' ')
