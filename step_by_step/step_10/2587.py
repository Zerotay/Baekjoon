import sys

input = sys.stdin.readline

inlst = []
for _ in range(5):
    inlst.append(int(input()))
print(sum(inlst) // 5)
print(sorted(inlst)[2])
