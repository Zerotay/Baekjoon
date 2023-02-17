n = int(input())
inlst = [*map(int, input().split())]
#원래 입력값은 자식을 인덱스로 해서 자신의 부모를 가리키는 배열.

lst = [[] for _ in range(n)]
for i, j in enumerate(inlst):
	if j == -1: continue
	lst[j].append(i)
#트리 생성. lst에는 부모를 인덱스로 해 자식에 대한 정보가 담긴다.

dp = [0 for _ in range(n)]
# 각 원소는 자기 자신을 루트라고 쳤을 때 아래로 전파되는데 걸리는 최소 시간

def recur(num):
	tmp = []
	for i in lst[num]:
		recur(i)
		tmp.append(dp[i]) #부하들의 dp가 담긴다.
	if tmp: #자식이 없으면 들어오지 않고, 그 다음부터 아래 1층부터 들어온다.
		tmp.sort(reverse=True)
		#아래에서 이뤄질 과정을 위해 정렬
		#큰 순서로 정렬하는 이유는 자식이 많은 쪽을 먼저 가야 그나마 최단이라.
		time = [tmp[i] + i + 1 for i in range(len(tmp))]
		#tmp[i]는 자식이 가진 최소 시간.
		#i+1은 큰 자식부터 1씩의 시간을 늘려가는 것을 뜻한다.
		#즉 자식이 많은 놈에게 먼저 1의 시간을 투자하고, 그 다음 놈에게 2, ..
		#time은 전체적으로 시간이 최소한이 되도록 자식들에게 전파하는 시간을 담은 배열
		dp[num] = max(time) #그 중에서 가장 큰 값이 해당 dp. 즉 최소 시간.

recur(0)
print(dp[0])

# n = int(input())
# if n == 1:print(0); exit()

# arr = [*map(int, input().split())]
# val = [[] for _ in range(n)]
# up = [0] * n

# for x in arr[1:]:
#     up[x] += 1

# q = __import__('collections').deque()
# for i in range(1, len(arr)):
#     if up[i] == 0:
#         q.append([i, 0])
# while q:
#     x, t = q.popleft()
#     if x == 0: print(t)
#     nx = arr[x]
#     val[nx].append(t + 1)
#     up[nx] -= 1
#     if up[nx] == 0:
#         val[nx].sort(reverse=True)
#         nt = [val[nx][i] + i for i in range(len(val[nx]))]
#         q.append([nx, max(nt)])