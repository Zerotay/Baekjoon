import sys

input = sys.stdin.readline
print = sys.stdout.write

num, k = map(int, (input().split(" ")))
lst = list(map(int, input().split(" ")))
lst.sort(reverse=True)
print(str(lst[k - 1]))