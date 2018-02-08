def rms(string):
    new = ''
    i = 0
    while i < len(string):
        if string[i] not in new:
            new = new + string[i]
            i = i + 1
        else:
            i = i + 1
    return(new)
