n = int(input())
inlst = list(map(int, input().split()))
inlst.sort()
lst = [0] * (n + 1)
for i in range(n):
	lst[i] = lst[i-1] + inlst[i]
print(sum(lst))