S = 4
S1 = 0
L = 3
L1 = 0
M = 5
M1 = 0
T_S = S + L + M
while True:
    shirt_type = input('enter shirt type "S","M" or "L": '.title())
    if shirt_type == "S":
        if S1 < S:
            S1 += 1
        else:
            print('we dont have "S" size shirts more then',S)
    elif shirt_type == "L":
        if L1 < L:
            L1 += 1
        else:
            print('we dont have "L" size shirts more then',L)
    elif shirt_type == "M":
        if M1 < M:
            M1 += 1
        else:
            print('we dont have "M" size shirts more then',M)
    elif shirt_type == "e":
        ans = input('are u sure u want to end this shopping: ')
        if ans == "y":
            break
        else:
            pass
    if T_S == S1 + L1 + M1:
        print('we dont have more then this.'.title())
        break
    else:
        pass
