a = input("> ")
list1 = a.split()
list2 = []

while len(list1) > 1:
	b = list1[0]
	list1.pop(0)
	list2.append(b)
	c = list1[0]
	list1.pop(0)
	list1.append(c)

list2.append(list1[0])
print(list2)