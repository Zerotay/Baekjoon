n = int(input())
inlst = input().split()

ans = set()
minval = 'Z'
ind = 0
check = 0
for i in range(n):
	if minval == inlst[i][0]:
		check = 1
	if minval > inlst[i][0]:
		ind = i
		check = 0
		minval = inlst[i][0]
if check:
	for i in range(n):
		if inlst[ind][0] <= inlst[i][1]:ans.add(inlst[i][1])
else:
	for i in range(n):
		if i == ind: continue
		if inlst[ind][0] <= inlst[i][1]:ans.add(inlst[i][1])

minval = 'Z'
ind = 0
check = 0
for i in range(n):
	if minval == inlst[i][0]:
		check = 1
	if minval > inlst[i][1]:
		ind = i
		check = 0
		minval = inlst[i][1]

if check:
	for i in range(n):
		if inlst[ind][1] <= inlst[i][0]:ans.add(inlst[i][0])
else:
	for i in range(n):
		if i == ind: continue
		if inlst[ind][1] <= inlst[i][0]:ans.add(inlst[i][0])

print(len(ans))
print(*sorted(ans))



# n = int(input())
# inlst = map(int, input().split())
# cnter = Counter(inlst)
# lst = []
# for i in cnter:
# 	if cnter[i] > 1:
# 		lst.append(i)
# 		lst.append(i)
# 	else: lst.append(i)

# comb = map(lambda x: x[0] * x[1], combinations(lst, 2))
# ans = 0
# for i in comb:
# 	tmp = sum(int(j) for j in str(i))
# 	ans = max(ans, tmp)
# print(ans)