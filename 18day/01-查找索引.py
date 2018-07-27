list = [1,2,5,6,10,3,40,66,78]

num = int(input("请输入一个数字"))

if num in list:
	position = list.index(num)
	print("索引是%d"%position)
	print(list)
else:
	print("不在列表中")
