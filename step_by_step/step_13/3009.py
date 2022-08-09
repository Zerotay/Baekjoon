from collections import Counter

xlst = []
ylst = []
for i in range(3):
	x, y = map(int, input().split())
	xlst.append(x)
	ylst.append(y)
countx = Counter(xlst)
county = Counter(ylst)
print(countx.most_common(2)[1][0], county.most_common(2)[1][0])
