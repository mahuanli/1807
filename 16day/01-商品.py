list = []
def shangjia():
	good = {}
	name = input("请输入名字")
	count = input("请输入商品上架数量")
	price = float(input("请输入商品价格"))
	good["name"] = name
	good["count"] = count
	good["price"] = price

	list.append(good)



def buy():
	name = input("请输入商品名字")
	for good in list:
		for good["name"] == name:
			count = int(input("请输入购买数量"))
			mygood["name"] = name
			mygood["count"] = count
			mygood["price"] = good["price"]
			good["count"] = good["count"] - count
			buylist.append(mygood)

