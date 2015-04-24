def versioncheck(v1,v2):
	list1=[ ]
	list2=[ ]
if v1==0 and v2==0:
		return 0
	elif v1==0:
		return -1
	elif v2==0:
		return 1
	
	l1=len(v1)
	l2=len(v2)

	if l1>l2:
		return 1
	elif l2<l1:
		return -1
	else:
		for i in v1:
 if i.isdigit():
	list1.append(i)
x=‘ ‘.join(list1)
for i in v2:
	if i.isdigit():
		list2.append(i)
	y= ‘ ‘.join(list2)
	if x>y:
return 1
	elif x<y:
return -1
	else:
		return 0
	

