import sys

input = sys.stdin.readline

N, M = map(int, input().split())
inlst = [list(map(int, input().split())) for _ in range(N)]
for i, _ in enumerate(range(N)):
    tmp = list(map(int, input().split()))
    for j in range(M):
        inlst[i][j] += tmp[j]
        print(inlst[i][j], end=' ')
    print()
