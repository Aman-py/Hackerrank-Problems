def reverse(string):
    i = len(string)-1
    rev = ''
    while i != -1:
        rev = rev + string[i]
        i = i-1
    return(rev)
