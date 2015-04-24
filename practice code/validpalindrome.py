def valid_palindrome(s):
    if s==None:
        return None
    s=s.lower()
    length=len(s)
    i=0
    j=length-1
    if length==0:
        return True
    while j>=i:
        while j>i and not s[i].isalnum():
            i+=1
        while j>i and not s[j].isalnum():
            j-=1
        if s[i]==s[j]:
            i+=1
            j-=1
        else:
            return False
    return True
