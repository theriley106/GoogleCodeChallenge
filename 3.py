a = [2, 5, 7, 12, 19, 31]

count = len(a)

while count < 40:
	print a[-1]
	print a[-2]
	#print("{} - {}".format([a[-1], a[-2]]))
	a.append(sum([a[-1], a[-2]]))
	count += 1

print a[39]



