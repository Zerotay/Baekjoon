import sys

input = sys.stdin.readline

lst = [0 for _ in range(30)]
for _ in range(28):
    tmp = int(input())
    lst[tmp-1] = 1
for i,j in enumerate(lst):
    if j == 0:
        print(i+1)
