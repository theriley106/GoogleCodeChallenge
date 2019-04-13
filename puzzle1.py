def calc(i):
	points = i
	found = False
	if i % 3 == 0:
		found = True
		finalPoints = points * 2
	if i % 5 == 0:
		found = True
		finalPoints = points * 3
	if i % 15 == 0:
		found = True
		finalPoints = points * 10
	if found == False:
		return points
	return finalPoints
a = []
for i in range(1, 1001):
	a.append(calc(i))
print sum(a)
