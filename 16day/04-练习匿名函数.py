def clum1(x,y,z):
	ret = z(x,y)
	return ret
ret = clum1(1,2,lambda x,y:x-y)
print(ret)
'''
ret = clum(1,2,"-")
print(ret)
'''

'''
print(z)打印匿名函数地址
ret = clum1(1,2,lambda x,y:x+y)
print(ret)
print(clum)打印函数地址
'''
