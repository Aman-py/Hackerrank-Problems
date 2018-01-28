secret_num = '5'
while True:
    number_guess = input('enter your number between 1 to 5: '.title())
    if number_guess == secret_num:
        print('great u got that'.title())
        break
    else:
        print('better luck next time'.title())
