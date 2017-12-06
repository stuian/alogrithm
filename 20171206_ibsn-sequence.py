#输入有 2 行，第 1 行为一个正整数，表示有 n 个同学参与调查（n≤100）。第 2 行有 n 个用空格隔开的正整数，为每本图书的 ISBN号（假设图书的 ISBN号在 1~1000之间）。 输出也是 2行，第 1行为一个正整数 k，表示需要买多少本书。
#第 2行为 k个用空格隔 开的正整数，为从小到大已排好序的需要购买的图书的 ISBN号

a = input("> ")
b = input()

list1 = b.split()
list2 = []

for i in list1:
	if i not in list2:
		list2.append(i)

print(len(list2))
print(list2)