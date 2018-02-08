def sort(string):
    temp = ''
    i = 0
    while i < len(string):
        new = string
        temp = temp + min(new)
        new.replace(min(new),'z',1)
        i = i + 1
    return(temp)
        
