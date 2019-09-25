from POPTOK_functions import *

num = ' '
while True:
    num = input('give me a number')
    if num.isnumeric():
        num = int(num)
        if num_div3(num) and num_div5(num):
                print('POPTOK')
        elif num_div5(num):
                print('TOK')
        elif  num_div3(num):
                print('POP')
        else:
                print(num)
    elif num == 'potato':
        print('thanks for playing!!!!!')
        break
    else:
        print('this is not a number!!!!!')



# we will need to import our functions

# play the game and while loop here