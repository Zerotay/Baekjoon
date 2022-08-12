import sys

input = sys.stdin.readline
def cal(val, signal, num):
	if signal == 0:
		return val + lst[num]
	elif signal == 1:
		return val - lst[num]
	elif signal == 2:
		return val * lst[num]
	else:
		if val < 0:
			return val * -1 // lst[num] * -1
		else:
			return val // lst[num]

def dfs(val, num):
	if num == n:
		answer.append(val)
		return
	else:
		for i in range(4):
			if sig[i] != 0:
				sig[i] -= 1
				dfs(cal(val, i, num), num + 1)
				sig[i] += 1

n = int(input())
lst = list(map(int, input().split()))
sig = list(map(int, input().split()))
val = lst[0]
answer = []
dfs(val, 1)
print(max(answer), min(answer))