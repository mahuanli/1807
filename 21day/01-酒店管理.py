import time
list = []
#每秒十元
money = 0
def ruzhu():
	info = {}
	name = input("请输入名字")
	while True:
		sfz = int(input("请输入你的身份证"))
		if len(sfz) == 18:
			return
		break
	else:
		print("重新输入")

info["name"] = name
info["sfz"] = sfz
info["ctime"] = int(time.time())
list.append(info)
priint(list)
def lidian():
	global money
	name = input("请输入名字")
	for i in list:
		if name == i["name"]:
			entime = int(time.time())
			money +=(entime-i["ctime"])*10
			list.remove(i)
			print("酒店赚了%.02f"%money)
			break
def print_menu():
	while True:
		print("1.入住")
		print("2.离店")
