import sys
from collections import Counter

input = sys.stdin.readline
n  = int(input())
nlst = list(map(int, input().split()))
m = int(input())
mlst = list(map(int, input().split()))
count = Counter(nlst)
for i in mlst:
	print(count[i], end=" ")