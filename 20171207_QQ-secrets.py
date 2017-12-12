#解密QQ号，输入9个数字，每一次删除第一个数，并把第二个数移动最后，最后剩一个数字，删除。
#最终删除的数字按删除顺序排列好就是要得到的QQ号

#方法：设置一个list，长度为11，从第二位开始，list[1]为head，list[10]为tail
#每次删除第一个数，head往后移一位，最后增加一个数，tail往后移一位。
#保证head和tail之间为有效数字。
#队列是一种特殊的线性结构，它只允许在队列的首部（head）进行删除操作，这称为“出队”，而在队列 的尾部（tail）进行插入操作，这称为“入队”

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