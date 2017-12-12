#纸牌游戏——小猫钓鱼
#队列和栈的结合应用
#题目描述：
#星期天小哼和小哈约在一起玩桌游，他们正在玩一个非常古怪的扑克游戏——“小猫钓
#鱼”。游戏的规则是这样的：将一副扑克牌平均分成两份，每人拿一份。小哼先拿出手中的
#第一张扑克牌放在桌上，然后小哈也拿出手中的第一张扑克牌，并放在小哼刚打出的扑克牌
#的上面，就像这样两人交替出牌。出牌时，如果某人打出的牌与桌上某张牌的牌面相同，即
#可将两张相同的牌及其中间所夹的牌全部取走，并依次放到自己手中牌的末尾。当任意一人 手中的牌全部出完时，游戏结束，对手获胜。 
#假如游戏开始时，小哼手中有 6张牌，顺序为 2 4 1 2 5 6，小哈手中也有 6张牌，顺序 为 3 1 3 5 6 4，终谁会获胜呢？现在你可以拿出纸牌来试一试。接下来请你写一个程序来 自动判断谁将获胜。这里我们做一个约定，小哼和小哈手中牌的牌面只有 1~9

#队列1
list1 = [0 2 4 1 2 5 6] 
#加0是为了让序号从1开始
#队列2
list2 = [0 3 1 3 5 6 4]

#栈
list3 = []

def out_queue(head,tail):
	for i,j in zip(range(head1,tail1),range(head2,tail2)):
		if i in list3:
			list4 = list3[list3.index(i):]
			list4.append(i)
			#出栈
			for indx in range(list3.index(i),len(list3)):
				list3.pop(indx)
			#入队list1
			x = len(list4)-1
			while x >= 0:
				list1.append(list4[x])
		if j in list3:
			list5 = list3[list3.index(j):]
			list5.append(j)
			#出栈
			for idx in range(list3.index(j),len(list3)):
				list3.pop(idx)
			#入队list2
			x = len(list5)-1
			while x >= 0:
				list2.append(list5[x])
		else:
			list3.append(i)
			list3.append(j)