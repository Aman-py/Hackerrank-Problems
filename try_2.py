
# coding: utf-8

# In[2]:


kadu = int(input('enter your age: '.title()))


# In[3]:


weight1 = '60' # a string
weight2 = 170 # an integer
# add 2 integers
total_weight = int(weight1) + weight2
print(total_weight)


# In[4]:


str_num_1 = "11"
str_num_2 = "15"
int_num_3 = 10
name = int(str_num_1) + int(str_num_2) + int_num_3
print(name)


# In[5]:


str_integer = "2"
int_number = 10
number_total = int(str_integer) + int_number
print(number_total)


# In[6]:


student_age = input('enter student age (integer): ')
age_next_year = int(student_age) + 1
print('Next year student will be',age_next_year)


# In[7]:


num_1 = input('type your 1st int.: '.title())
num_2 = input('type your 2nd int.: '.title())
print(int(num_1) + int(num_2))


# In[13]:


if response == 3:
    return "Correct"
elif response <= 0:
    return "Correct"
else:
    return "Incorrect"
  


# In[15]:


x = 3
y = "3" 

# get_diff takes an int and a str
def get_diff(xint, ystr):
    return int(ystr) - xint
    

if y.isdigit() == False:
   print('"y" is not an integer string')
elif get_diff(x,y) == 0:
    print('x equal to y')
else:
    print('x is NOT equal to y')


# In[16]:


size_num = "8 9 10"

size = "8" # user input

if size.isdigit() == False:
    print("Invalid: size should only use digits")
elif int(size) < 8:
    print("size is too low")
elif size in size_num:
    print("size is recorded")
else:
    print("size is too high")


# In[17]:


print("3 + 5 =",3 + 5)
print("3 + 5 - 9 =", 3 + 5 - 9)
print("48/9 =", 48/9)
print("5*5 =", 5*5)
print("(14 - 8)*(19/4) =", (14 - 8)*(19/4))


# In[18]:


def million_maker():
    make_big = input("enter a non-decimal number you wish were bigger: ")
    return int(make_big)*1000000

print("Now you have", million_maker())


# In[1]:


def million_maker():
    make_big = input("enter a non-decimal number you wish were bigger: ")
    return int(make_big)*1000000


# In[2]:


million_maker()


# In[22]:


15*43


# In[23]:


156/12


# In[24]:


21/.5


# In[25]:


111 + 84 - 45


# In[26]:


(21 + 4)*4


# In[27]:


def calculator():
    num_1 = input('enter your num: '.title())
    num_2 = input('enter your num: '.title())
    returne= int(num_1)*int(num_2)
    return returne


# In[28]:


calculator()


# In[9]:


def calculator(operator):
    num_1 = input('enter your num: '.title())
    num_2 = input('enter your num: '.title())
    op_1 = int(num_1)*int(num_2)
    op_2 = int(num_1)/int(num_2)
    return if operator == *:


# In[32]:


student_name = input("enter name: ").capitalize()
if student_name.startswith("F"):
    print(student_name,"Congratulations, names starting with 'F' get to go first today!")
elif student_name.startswith("G"):
    print(student_name,"Congratulations, names starting with 'G' get to go second today!")
else:
    print(student_name, "please wait for students with names staring with 'F' and 'G' to go first today.")


# In[37]:


calculator(returne)


# In[48]:


calculator(operator)


# In[ ]:


calculator(operator)


# In[1]:


# This function adds two numbers 
def add(x, y):
   return x + y

# This function subtracts two numbers 
def subtract(x, y):
   return x - y

# This function multiplies two numbers
def multiply(x, y):
   return x * y

# This function divides two numbers
def divide(x, y):
   return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Take input from the user 
choice = input("Enter choice(1/2/3/4):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")


# In[1]:


def multiply(x,y):
    return x*y
def devide(x,y):
    return x/y
print('operation u want to do \n1. Multiply \n2.devide'.title())
operation = input('input operation no.: '.title())
num_1 = int(input('enter your 1st num: '.title()))
num_2 = int(input('enter your 2nd num: '.title()))
if operation == '1':
    print(num_1,'*',num_2,'=',multiply(num_1,num_2))
elif operation == '2':
    print(num_1,'/',num_2,'=',devide(num_1,num_2))
else:
    print('invalid operation'.title())


# In[2]:


x = 3
y = 4
calculation = x*y
print(calculation)


# In[3]:


calculation = 5 + 15 / 5 + 3 * 2 - 1
print(calculation)


# In[3]:


secret_num = 2
def check_guess(x,y):
    guess = input('guess your 1st answer: '.title())
    return guess
if guess == secret_num:
    print('your guess is right')
elif guess != secret_num:
    print('try next time')
    check_guess(x,y)
else:
    pass


# In[9]:


fav_color = input('type your fav. color(ROYGBIV): '.title()).upper()
if fav_color == 'R':
    print('your fav. color is red'.title())
elif fav_color == 'O':
    print('your fav. color is orange'.title())
elif fav_color == 'Y':
    print('your fav. color is yellow'.title())
elif fav_color == 'G':
    print('your fav. color is green'.title())
elif fav_color == 'B':
    print('your fav. color is blue'.title())
elif fav_color == 'I':
    print('your fav. color is indigo'.title())
elif fav_color == 'V':
    print('your fav. color is voilet'.title())
else:
    print('title not match'.title())


# In[10]:


fav_color = input('type your fav. color(ROYGBIV): '.title()).upper()
if fav_color == 'R':
    print('your fav. color is red'.title())
elif fav_color == 'O':
    print('your fav. color is orange'.title())
elif fav_color == 'Y':
    print('your fav. color is yellow'.title())
elif fav_color == 'G':
    print('your fav. color is green'.title())
elif fav_color == 'B':
    print('your fav. color is blue'.title())
elif fav_color == 'I':
    print('your fav. color is indigo'.title())
elif fav_color == 'V':
    print('your fav. color is voilet'.title())
else:
    print('title not match'.title())


# In[18]:


fav_color = input('type your fav. color(ROYGBIV): '.title()).upper()
if fav_color == 'R':
    print('your fav. color is red'.title())
elif fav_color == 'O':
    print('your fav. color is orange'.title())
elif fav_color == 'Y':
    print('your fav. color is yellow'.title())
elif fav_color == 'G':
    print('your fav. color is green'.title())
elif fav_color == 'B':
    print('your fav. color is blue'.title())
elif fav_color == 'I':
    print('your fav. color is indigo'.title())
elif fav_color == 'V':
    print('your fav. color is voilet'.title())
else:
    print('title not match'.title())


# In[15]:


def rainbow_color():
    fav.color = input('enter your fav. color: ')


# In[1]:


fav_color = input('enter your fav.color: ')
def rainbow_color():
    return fav_color
rainbow_colors = ('red,green,indigo,voilet,blue,yellow,orange')
if rainbow_color() in rainbow_colors:
    print('your fav_color is',rainbow_color())
else:
    print('no match')


# In[36]:


rainbow_color()


# In[29]:


rainbow_color()


# In[3]:


present_age = int(input('type your present age: '))
def age_20():
    if present_age > 20:
        sub_tract = present_age - 20
        return sub_tract,'5 years old, 20 years difference from now'
    elif present_age < 20:
        add = present_age + 20
        return add,'years old, 20 years difference from now'
    else:
        pass


# In[2]:


present_age = int(input('type your present age: '))
def age_20(present_age):
    if present_age > 20:
        sub_tract = present_age - 20
        return print(sub_tract,"years old, 20 years difference from now")
    elif present_age < 20:
        add = present_age + 20
        return print(add,'years old, 20 years difference from now')
    else:
        pass


# In[16]:


age_20(present_age)


# In[4]:


your_choice = input('type any digit or alphabet: ')
def rainbow_age_20(your_choice):
    if your_choice.isdigit() == True:
        return age_20(present_age)
    elif your_choice.isalpha() == True:
        return rainbow_color()
    else:
        return false


# In[6]:


your_choice = input('type any digit or alphabet: ')
def rainbow_age_20(your_choice):
    if your_choice.isdigit() == True:
        return print(age_20(present_age))
    elif your_choice.isalpha() == True:
        return print(rainbow_color())
    else:
        return false


# In[7]:


rainbow_color()


# In[8]:


age_20(present_age)


# In[9]:


rainbow_age_20(your_choice)


# In[10]:


your_choice = input('type any digit or alphabet: ')
def rainbow_age_20(your_choice):
    if your_choice.isdigit() == True:
        return print(age_20(present_age))
    elif your_choice.isalpha() == True:
        return print(rainbow_color())
    else:
        return false


# In[11]:


rainbow_age_20(your_choice)


# In[15]:


your_choice = input('type any digit or alphabet: ')
def rainbow_age_20(your_choice):
    if your_choice.isdigit() == True:
        return print(age_20(present_age))
    elif your_choice.isalpha() == True:
        return print(rainbow_color())
    else:
        return 'false'


# In[16]:


rainbow_age_20(your_choice)


# In[23]:


fav_color = input('enter your fav.color: ')
def rainbow_color(fav_color):
    rainbow_colors = ('red,green,indigo,voilet,blue,yellow,orange')
    if rainbow_color(fav_color) in rainbow_colors:
        return print('your fav_color is',rainbow_color(fav_color))
    else:
        print('no match')


# In[24]:


rainbow_color(fav_color)


# In[1]:


num_1 = int(input('enter your fav. no.: '))
num_2 = int(input('enter your fav. no.: '))
def average(num_1,num_2):
    return (num_1 + num_2)/2


# In[2]:


average(num_1,num_2)


# In[3]:


num_1 = int(input('enter your fav. no.: '))
num_2 = int(input('enter your fav. no.: '))
if num_1 > num_2:
    print(num_1 - num_2)
elif num_2 > num_1:
    print(num_2 - num_1)
else:
    pass


# In[5]:


num_1 = int(input('enter your fav. no.: '))
num_2 = int(input('enter your fav. no.: '))
if num_1 > num_2:
    print(int(num_1 / num_2))
elif num_2 > num_1:
    print(int(num_2 / num_1))
else:
    pass


# In[6]:


num_1 = int(input('enter your fav. no.: '))
num_2 = int(input('enter your fav. no.: '))
if num_1 > num_2:
    print(int(num_1 / num_2))
elif num_2 > num_1:
    print(int(num_2 / num_1))
else:
    pass


# In[12]:


chese = float(input('Enter cheese order weight (numeric value): '))
costs = chese * 7.9
if chese >= 100:
    print(chese,'is more than currently available stock')
elif chese <= .50:
    print(chese,'is below minimum order amount')
else:
    print(chese,'costs','$',costs)


# In[13]:


sandwich_type = input('"c" for Cheese or "v" for Veggie Special: ')

if sandwich_type.lower() == "c":
    # select cheese type
    cheese_type = input('"c" for Cheddar or "m" for Manchego: ')
    
    if cheese_type.lower() == "c":
        print("Here is your Cheddar Cheese sandwich")
    else:
        print("Here is your Manchego Cheese sandwich") 

else:
    print("Here is your Veggie Special")


# In[14]:


sandwich_type = input('"c" for Cheese or "v" for Veggie Special: ')

if sandwich_type.lower() == "c":
    # select cheese type
    cheese_type = input('"c" for Cheddar or "m" for Manchego: ')
    
    if cheese_type.lower() == "c":
        print("Here is your Cheddar Cheese sandwich")
    else:
        print("Here is your Manchego Cheese sandwich") 

else:
    print("Here is your Veggie Special")


# In[15]:


print("Hi, welcome to the sandwich shop.  Please select a sandwich.")
sandwich_type = input('"c" for Cheese or "v" for Veggie Special: ')
# select sandwich type sandwich_type = input('"c" for Cheese or "v" for Veggie Special: ')
print()
    
if sandwich_type.lower() == "c":
    # select cheese type
    print("Please select a cheese.")
    cheese_type = input('"c" for Cheddar or "m" for Manchego: ')
    print()
    
    if cheese_type.lower() == "c":
        print("Here is your Cheddar Cheese sandwich.  Thank you.")
    elif cheese_type.lower() == "m":
        print("Here is your Manchego Cheese sandwich.  Thank you.") 
    else:
        print("Sorry, we don't have", cheese_type, "choice today.")

elif sandwich_type.lower() == "v":
    print("Here is your Veggie Special. Thank you.")
        
else:
    print("Sorry, we don't have", sandwich_type, "choice today.")
print()
print("Goodbye!")


# In[18]:


bird_names = ('hen,cock,duck,peacock')
bird_guess = input('type your 1st bird: '.title())
if bird_guess not in bird_names:
    bird_guess2 = input('type your 2nd bird: '.title())
    if bird_guess2 not in bird_names:
        bird_guess3 = input('type your 3rd bird: '.title())
        if bird_guess3 not in bird_names:
            print('better luck try next time'.title())
        else:
            print(bird_guess3,'is your 3rd guess but its right'.title())
    else:
        print(bird_guess2,'is your 2nd guess but its right'.title())
else:
     print(bird_guess,'is your 1st guess but its right'.title())


# In[2]:


if True:
    if False:
        print("Banana")
    else:
        print("Apple")
else:
    if True:
        print("Dates")
    else:
        print("Corn")


# In[3]:


print('hello python\ntoday i m in collage')


# In[1]:


student_age = input('type your age: ')
student_name = input('enter your name: ')
print('STUDENT NAME\t\tAGE')
print(student_name,'\t',student_age)


# In[2]:


print("\"quotes in quotes\"")


# In[3]:


print('what can i do \\n')


# In[4]:


print('what can i do\\n')


# In[6]:


print("\"\\\WARNING!///\"")


# In[5]:


word = input('type your word: '.title())
def pre_word():
    if word.startswith('pre') == True:
        pass
        if word.isalpha() == True:
            return print('TRUE')
        else:
            pass
    else:
        return print('FALSE')


# In[6]:


pre_word()


# In[7]:


print("Hello" + '\n' + "World!")


# In[2]:


# review and run GREET COUNT
greet_count = 5

# loop while count is greater than 0
while greet_count > 0:
    print(greet_count, "!")
    greet_count -= 1
    
print("\nIGNITION!")


# In[1]:


animal_num = 4
while animal_num > 0:
    animal_name = input('enter your animal name or exit: '.title())
    if animal_name == 'exit':
        break
    else:
        animal_num -= 1
        print('next animal name'.title())
        animal_names = animal_name
print(animal_names)


# In[2]:


num_animals = 0
max_animals = 4
animal_name = ""
all_animals = ""
animal_temp = ""
 
while num_animals <= 4:
 
    animal_name = input("Name an animal or \"exit\" to exit: \t")
    all_animals = animal_temp + animal_name
    animal_temp = all_animals
   
    if animal_name == "exit":
        print("***SESSION ENDED***")
        break
       
    elif animal_name.isalpha():
        print(animal_name )
    else:
        print("invalid entry")
    num_animals += 1
    if num_animals >= max_animals:
        print("\nNo more entrys allowed")
        print()
        break
print(all_animals)


# In[1]:


n = int(input('enter your no.: '))
num_group = 2,4
num_group2 = 6,8,10,12,14,16,18,20
if n in num_group:
    print('not weird')
elif n in num_group2:
    print('weird')
elif n/2 == float:
    print('weird')
elif n > 20:
    if n/2 == int:
        print('not weird')


# In[1]:


year = int(input())
def is_leap(year):
    leap = False
    leap2 = True
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return leap2
            else:
                return leap
        else:
            return leap2
    else:
        return leap
print(is_leap(year))


# In[1]:


num = int(input())
var = num/4
if type(var) == int:
    print('true')
else:
    print('false')


# In[2]:


print(is_leap(year))


# In[ ]:


n = int(input())
if n > 123:
    print('123',)

