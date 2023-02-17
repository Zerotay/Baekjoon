import sys

input = sys.stdin.readline
n, m = map(int, input().split())
nset = set(map(int, input().split()))
mset = set(map(int, input().split()))
print(len(nset ^ mset))