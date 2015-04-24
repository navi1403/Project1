def mergelist(A,m,B,n):
	new_list=[]
	if A==None and B==None:
	    return None
	elif A==None and B!=None:
		return B
	elif B==None and A!=None:
		return A
	i=0
	j=0
	while i<m and j<n:
		if A[i]<=B[j]:
		    new_list.append(A[i])
		    i+=1
		else:
		    new_list.append(B[j])
		    j+=1
	if i==m and j==n:
	    return new_list
	elif i==m and j<n:
	    while j<n:
	        new_list.append(B[j])
	        j+=1
	elif j==n and i<m:
	    while i<m:
	        new_list.append(A[i])
	        i+=1
	return new_list  


