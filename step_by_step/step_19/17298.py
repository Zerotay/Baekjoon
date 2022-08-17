n = int(input())
inlst = list(map(int, input().split()))
lst = [-1 for i in range(n)]
stack = []
for i in range(n):
	while stack and inlst[stack[-1]] < inlst[i]:
		lst[stack.pop()] = inlst[i]
	stack.append(i)
print(*lst)
