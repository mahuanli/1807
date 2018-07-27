list = []
def showError(msg):
	print("输入有误,请从新输入"+msg)
def is Num(num):
	if num.isdigit()
		return True
	else:
		return false
def add():
	stu = {}
	while True:
		name = input("请输入学生姓名")
		if len(name) >= 2 and len(name)<=4:
			stu["name"] = name
			break
		else:
			showError("学生姓名必须大于2小于4")
	while True:
		age = input("请输入学生年龄")
	if age > 1 and age < 130:
		stu["age"] = age
		break
	else:
		showError("年龄必须大于1小于130")
def delete():
	pass
def change():
	name = input("请输入要修改的名字")
	for stu in list:
		if stu["name"] == name:
			flag = 	True
			while True:
				print("1,修改名字")
				print("2,修改年龄")
				num = input("请选择功能")
				if isNum(num):
					num = int(num)
				else:
					print("输入有误")
					continue
			if num == 1:
				name = input("请输入新的名字")
				stu["name"] = name
			elif num == 2:
				age = int(input("请输入新的年龄"))
				stu["age"] = age
			break
		break
	if not flag:
		print("查无此人")
def find():
	find = input("请输入查找的学生姓名")
	for i in list:
		if i["name"]==find:
			print("\n姓名为:%s\n性别为%s\n"%(i["name"],i["sex"]))

def print_list():
	print("姓名        年龄")
	for stu in list:

def print_menu():
	print("欢迎进入学生管理系统".center(30," "))
	while True:
		print("1,增加学生信息")
		print("2,删除学生信息")
		print("3,更改学生信息")
		print("4,查找学生信息")
		print("5,打印学生信息")
		print("6,退出学生系统")
		input_info()

def input_info():
	num = int(input("请选择功能"))
	if num == 1:
		add()
	elif num ==2:
		find()
	elif num ==3
		change()
	elif num ==4:
		find()
print_menu()
