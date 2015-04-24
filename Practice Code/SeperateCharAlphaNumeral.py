def sepchar(s):
    char_list=[ ]
    my_list=[ ]
    num_list=[ ]
    alpha_list=[ ]
    if s==None or len(s)==0:
        return None
    for i in s:
        if i.isdigit()== True:
            num_list.append(i)
        elif i.isalpha()== True:
	        alpha_list.append(i)
        else:
            char_list.append(i)
            
    return num_list, alpha_list, char_list
