import sys

input = sys.stdin.readline

lst = [[0] * 100 for _ in range(100)]

for _ in range(int(input())):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            lst[x+i][y+j] = 1
ans = 0
for i in lst:
    for j in i:
        if j:
            ans += 1
print(ans)