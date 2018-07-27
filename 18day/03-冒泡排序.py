list = [8,6,23,1,3,10,7,98,80]





for i in range(0,len(list)-1)
	for j in range(i+1,len(list)):
		if list[i] > list[j]:
		 list[i],list[j] = list[j],list[i]n`
