
def using_hash(x,y):				#Calculates count using a dictionary/hash table
    count = 0					#initialize variable
    my_dict = {}					#initialize dictionary
    for i in range(x, y+1):			#loop through all the elements in the given range
        key = get_new_number(i)		#Call function to get a new number
        val = my_dict.get(key)			#Get value for key
        if val == None:				#If key does not exist
							
            my_dict[key] = 1			#Insert key with value 1       
else:			
            my_dict[key] = val+1			#increase value by 1
						
    for i in my_dict.values():			#loop through dict values 
        count += int(i*(i-1)/2)			#Calculate number of pairs 

    return count				#return the count

def get_new_number(num):			#Function to get digits from a number
    my_list=[]					#initialize the list
    while num>0:				#check if number is greater than 0
        my_list.append(str(num%10))	#get the last digit of a number and insert it into a list
        num=int(num/10)		#divide number by 10
    my_list.sort()			#sort the list
    return ''.join(my_list)		#join the list to return a sorted number
    
def are_equal(num1, num2):		#Function checks if numbers are equal		
	x = get_new_number(num1) #calls the get_new_number function
	y = get_new_number(num2)
	if x==y:			# checks if x is equal to y
		return True
	else:
		return False

def using_loops(x,y):				#Find count using loops	
    count = 0					#initialize count to 0
    for i in range(x, y+1):			#loop through the given range
      for j in range(i+1, y+1):	#loop through the range to compare each number with the number which i is pointing to
            if (are_equal(i,j)):			#call function to check if i is equal to j
                #print "(%d,%d)" %(i,j)		
                count=count+1
    return count
A=10
B=300
print using_loops(A,B)
print "now test hash"
print using_hash(A,B)

