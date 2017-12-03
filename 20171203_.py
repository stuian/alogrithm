#桶排序的缺点：1、占据大量的空间：如果是在2000000个数中取5个数比较大小，那就需要2000000个桶；2、如果比较小数怎么办
#冒泡排序（解决）

#冒泡排序的基本思想是：每次比较两个相邻的元素，如果它们的顺序错误就把它们交换过来。 
#“冒泡排序”的原理是：每一趟只能确定将一个数归位。

from sys import argv
import buckets_sequence

script,one,two,three,four = argv

list1 = [one,two,three,four]

list2 = buckets_sequence.buckets(one,two,three,four)
print(list2)

while list1 != list2:
	for index1,i in enumerate(list1):
		for index2,j in enumerate(list1):
			if index2 == index1 + 1:
				if list1[index1] < list1[index2]:
					c = list1[index1]
					list1[index1] = list1[index2] 
					list1[index2] = c
				else:
					pass
			else:
				pass

print(list1)
