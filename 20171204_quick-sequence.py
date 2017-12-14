#假如我 们的计算机每秒钟可以运行 10亿次，那么对 1亿个数进行排序，
#桶排序只需要 0.1秒，而冒 泡排序则需要 1千万秒，达到 115 天之久

#当然在坏的情况下，仍可能是相邻的两个数进行了交换。
#因此快速排序的差时间复杂度和 冒泡排序是一样的，都是 O(N2)，它的平均时间复杂度为 O (NlogN)。
#为什么必须要先从右边开始

# a = input("> ")
# b = a[::-1]

# # for index1,i in enumerate(b):
# # 	if i < a[0]:
# # 		sub1 = i

# for i in a:

# 	if i == 2:
# 		print(i)
# 		contiune

def QuickSort(arr,firstIndex,lastIndex):
    if firstIndex<lastIndex:
        divIndex=Partition(arr,firstIndex,lastIndex)
 
        QuickSort(arr,firstIndex,divIndex)       
        QuickSort(arr,divIndex+1,lastIndex)
    else:
        return
 
 
def Partition(arr,firstIndex,lastIndex):
    i=firstIndex-1
    for j in range(firstIndex,lastIndex):
        if arr[j]<=arr[lastIndex]:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[lastIndex]=arr[lastIndex],arr[i+1]
    print(i)
    return i
 
 
arr=[6,1,2,7,9,3,4,5,10,8]
 
print("initial array:\n",arr)
QuickSort(arr,0,len(arr)-1)
print("result array:\n",arr)

#一、 算法描述：
1．先从数列中取出一个数作为基准数。
2．分区过程，将比这个数大的数全放到它的右边，小于或等于它的数全放到它的左边。
3．再对左右区间重复第二步，直到各区间只有一个数
#-*- coding: utf-8 -*-
Def sub_sort(a):
Key = lst[head]
While head<tail:
if lst[tail]>key:
tail -= 1
	elif lst[tail]<key:
		if lst[head]>key:
			c = lst[head] 
			lst[head] = lst[tail]
			lst[tail] = c
	tail -= 1
	head += 1
		else:
			head += 1
