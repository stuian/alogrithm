#期末考试完了老师要将同 学们的分数按照从高到低排序。
#小哼的班上只有 5个同学，这 5个同学分别考了 5分、3分、 5分、2分和 8分，哎考得真是惨不忍睹（满分是 10分）。
#接下来将分数进行从大到小排序， 排序后是 8 5 5 3 2。你有没有什么好方法编写一段程序，让计算机随机读入 5个数然后将这 5个数从大到小输出？

# from sys import argv

# script,one,two,three,four = argv

# one = int(one)
# two = int(two)
# three = int(three)
# four = int(four)

# if one > = two:
# 	sequence_1 = str(one) + str(two)
# 	if three > = four:
# 		sequence_2 = str(three) + str(four)
# 	else:
# 		sequence_2 = str(four) + str(three)
# else:
# 	sequence_1 = str(two) + str(one)

# if three > = four:
# 	sequence_2 = str(three) + str(four)
# else:
# 	sequence_2 = str(four) + str(three)

#写不下去了，感觉会嵌套很多层if，else肯定不好
#--------------------------------------------------------

#理解错了，我以为是随便输入四个数，给它们排序

#桶排序

# from sys import argv

# script,one,two,three,four = argv

lst = [0,0,0,0,0,0,0,0,0,0,0]

#将0-10改为0-1000
# list1=[]
# for i in range(1001):
# 	list1.append(i)


a = []

def buckets(one,two,three,four):
	one = int(one)
	two = int(two)
	three = int(three)
	four = int(four)
	for i in one,two,three,four:
		lst[i] += 1
	for index,l in enumerate(lst):
		if l > 0:
			for i in range(l):
				# print(index)
				a.append(index)
	return a

#从大到小排列

#1 reversed()函数
# b =list(reversed(a))
# print(b)
# #2 sorted()函数
# c = sorted(a,key=None,reverse=True)
# print(c)
# #3
# d = a[::-1]
# print(d)