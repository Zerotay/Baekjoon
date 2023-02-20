import sys

input = sys.stdin.readline

ans = -1
position = [0,0]
for i in range(9):
    row = list(map(int, input().split()))
    max_val = max(row)
    if ans < max_val:
        ans = max_val
        position[0] = i + 1
        position[1] = row.index(max_val) + 1

print(ans)
print(*position)
