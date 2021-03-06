#队列是一种先进先出的数据结构，相反，栈是一种后进先出的结构
#例子：你往一桶里放球，如果要拿出来也必须要把后放进去的先拿出来，才能拿出最开始的球（假设桶的直径是球的直径）
#栈的结构：只需要一个一维数组和一个指向栈顶的变量 top就可以了。我们通过 top来对栈 进行插入和删除操作。

#判断一个字符串是否是回文字符串
#书中的方法：利用栈的方法，回文字符串是对称的，将前半部分字符串入栈
#出栈的时候于后半部分如果能一一对应，那么称这个字符串是回文字符串

a = input()
list1 = []
for j in a:
	list1.append(j)
i = len(a)
list2 = []
while i > 0 :
	list2.append(a[i-1])
	i = i-1

print(list2)
if list1 == list2:
	print("该字符串是回文字符串")
else:
	print("该字符串不是回文字符串")