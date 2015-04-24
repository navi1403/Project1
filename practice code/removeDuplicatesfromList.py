def remove_dup(in_list):
    print in_list
    if in_list == None:
        return None
        
    length = len(in_list)
    if length == 0 or length == 1:
        return in_list
    
    i =0
    while i < (length-1):
        j=i+1
        print i,in_list[i]
        if in_list[i]==in_list[j]:
            in_list.remove(in_list[j])
            length-=1
            print in_list, len(in_list)
        else:
            i = i+1
    print in_list
    return in_list
