def decToRoman(x):
	roman={}
	roman_number=[]
	roman={1: "I", 4: "IV", 5 : "V" , 9: "IX", 10: "X" , 40 : "XL" , 50 : "L" , 90: "XC" , 100: "C" , 400 : "CD" , 500 : "C", 900: "CM" , 1000: "M"}
	all_keys=roman.keys()
	all_keys.sort()
	
	print roman.keys()
	print all_keys
	
	if x==None:
	    return None
	while  x>0:
	    for i in range(0, len(all_keys)):
	        if x>=all_keys[i] and x<all_keys[i+1]:
	            roman_number.append(roman.get(all_keys[i]))
	            print all_keys[i]
	            print roman_number
	            break
	        #print x
	    x=x-all_keys[i]
	        #print x
	return ''.join(roman_number)
