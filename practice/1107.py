import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
inlst = []
if m: inlst = [*map(int, input().split())]

simple = abs(n - 100)
ans = simple
k = str(n)

check = True
while check:
	for i in range(len(k)):
		if int(k[i]) in inlst:
			break
		if i == len(k)-1:
			# print(ans, len(k) + abs(int(k) - n))
			if ans > len(k) + abs(int(k) - n):
				ans = len(k) + abs(int(k) - n)
				check = False

	k = str(int(k) - 1)
	if k == '0': break

# print(1)
check = True

while check:
	for i in range(len(k)):
		if int(k[i]) in inlst:
			break
		if i == len(k)-1:
			# print(ans, len(k) + abs(int(k) - n))
			if ans > len(k) + abs(int(k) - n):
				ans = len(k) + abs(int(k) - n)
				check = False
	k = str(int(k) + 1)
	if int(k) >= 1000000: break
print(ans)

# for i in range(1000000):
# 	k = str(i)
# 	for j in range(len(k)):
# 		if int(k[j]) in inlst: break
# 		if j == len(k)-1:
# 			ans = min(ans, len(k) + abs(int(k) - n))
# print(ans)
