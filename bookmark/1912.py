n = int(input())
inlst = [*map(int, input().split())]
lst = [0 for _ in range(n)]
lst[0] = inlst[0]
for i, j in enumerate(inlst[1:]): lst[i+1] = max(j, lst[i] + j)
print(max(lst))