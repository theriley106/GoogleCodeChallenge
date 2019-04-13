start = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
end = [4, 17, 13, 7, 1, 10, 8, 12, 11, 3, 19, 15, 9, 2, 18, 16, 6, 5, 0, 14]
db = {}
for i, val in enumerate(start):
	db[end.index(val)] = i

print db
def sortVal(listVal):
	for i, val in db.iteritems():
		a = int(listVal[i])
		a = [None] * len(listVal)
		for i in range(len(listVal)):
			a[i] = listVal[db[i]]
	return a

if __name__ == '__main__':
	count = 0
	tempStart = list(start)
	x = sortVal(start)
	while x != tempStart:
		x = sortVal(x)
		count += 1
	print count
