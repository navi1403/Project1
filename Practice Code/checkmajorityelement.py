def checkmajorityelement(n):
	my_dict={}
	for i in n:
		count = my_dict.get(i,0) + 1
		my_dict[i] = count
	if count > len(n)/2:
		return i

	return "Not found"


