
# coding: utf-8

# In[7]:


print('enter a small int:')
small_int = input()


# In[8]:


print('the small int is '+ small_int)


# In[9]:


print('Enter the student name')
student_name = input()


# In[10]:


student_name = input('enter lacochecks name')
print('hello '+student_name +' welcome')


# In[11]:


Name = input('Enter Your Name: ')
Age = input('Enter Your Age: ')
get_email = input('Yes or No: ')
print('Name = '+ Name)
print('Age = ' + Age)
print('wants email = ' + get_email )



# In[12]:


answer = input("enter your answer: ")  
print(10 + answer) 


# In[13]:


name = 'mukesh'


# In[14]:


print('hello',name,'welcom in my world')


# In[ ]:


print('nisha','fuck','u')


# In[ ]:


print('nisha','lets enjoy',69)


# In[ ]:


nisha = "0.5"
print('nisha i want to fuck u',nisha,'@$%')


# In[1]:


street = input('st. name')
street_no = input('st. no.')
print('i want to go',street,street_no)


# In[2]:


owner = input('enter name for contact person for training group: ') 
num_people = input('enter the total number attending the course: ') 
training_time = input('enter the training time selected: ')
min_early = input('input early min')
print('------------------------------ ')
print('Reminder: training is schedule a',training_time,'for the',owner,'group of',num_people,'attendees Please arrive',min_early,' minutes early for the first class')


# In[3]:


print('hello,"i m aman agarwal')


# In[4]:


print("i m here to 'fuck u' ")


# In[5]:


"hello".isalpha()


# In[6]:


'2sexy'.isalnum()


# In[9]:


answer = int()
answer = input()
x = 5
y = 10
z = x + y + answer
print(z)


# In[4]:


"Lacochecks Name".istitle()


# In[15]:


'1111111111111111111111111111111111111111111111111111111111111111111111111111111111'.isdigit()


# In[17]:


ans_wer = "1234567890"
ans_wer.isdigit()
print('my answer',ans_wer,'=',answer.isdigit())


# In[21]:


'save'.startswith('s')


# In[22]:


'hey'.islower()


# In[23]:


'sex'.isupper()


# In[24]:


'alphabetical'.isalpha()


# In[26]:


"Are spaces and punctuation Alphabetical?".isalpha()


# In[27]:


length = "33"
length.isalnum()


# In[29]:


print("ms. Browning is in her office.".capitalize())


# In[2]:


fav_color = "green"
print(fav_color.capitalize(), fav_color, fav_color,"and", fav_color.upper()+"!")


# In[3]:


print('HELLO , mukesh FROM NOW u are a LACOCHECK'.upper())


# In[4]:


print('HELLO , mukesh FROM NOW u are a LACOCHECK'.lower())


# In[5]:


print('HELLO , mukesh FROM NOW u are a LACOCHECK'.capitalize())


# In[6]:


print('HELLO , mukesh FROM NOW u are a LACOCHECK'.title())


# In[7]:


print('HELLO , mukesh FROM NOW u are a LACOCHECK'.swapcase())


# In[8]:


print('HELLO , mukesh FROM NOW u are a LACOCHECK'.())


# In[10]:


fav_food = input()
print(fav_food.upper())


# In[11]:


fav_color = input('my fav color is: '.title()).swapcase()
print(fav_color)


# In[12]:


color = 'blue,sexy,black.pitch.bread.dew,new,orange,crew,brown,glew,pink'
print('pink' in color)


# In[13]:


color = 'blue,sexy,black.pitch.bread.dew,new,orange,crew,brown,glew,pink'
print('pink in color: '.capitalize(),'pink' in color)


# In[18]:


name = "SKYE HOMSI"
print("Y" in name.lower())


# In[1]:


print('********************')
print('*                  *')
print('*                  *')
print('*                  *')
print('*                  *')
print('*                  *')
print('*                  *')
print('********************')


# In[4]:


print('*                  *')
print(' *                *')
print('  *              *')
print('   *            *')


# In[6]:


type('aakrsh')


# In[7]:


type(5)


# In[8]:


type(3.14)


# In[9]:


type("save your notebook" + 'aakrsh')


# In[10]:


stu_dent = "mukesh"
type(stu_dent)


# In[14]:


stud_ent = 5
type(stud_ent)


# In[15]:


stu_ent = 3.15
type(stu_ent)


# In[16]:


type(stud_ent + stu_ent)


# In[17]:


type(stu_dent+stud_ent)


# In[18]:


x = 1
y = 2
z = 3
xyz_sum = x+y+z
print(xyz_sum)


# In[19]:


remind_me = input('Alarm Time')
print('remind me: ',remind_me)


# In[20]:


meeting_sub = input('what is the meeting subject?: ')
meeting_time = input("what is the meeting time?: ")
print('Meeting Subject: ',meeting_sub)
print('Meeting Time: ',meeting_time)


# In[21]:


print("'")


# In[22]:


print('""""""""')


# In[23]:


vehicle = input()
print(vehicle.isalpha())


# In[25]:


vehicle = input()
print(vehicle.isalnum())


# In[26]:


vehicle = input()
print(vehicle.isdigit())


# In[29]:


vehicle = input()
print(vehicle.isupper())


# In[30]:


vehicle = input()
print(vehicle.islower())


# In[31]:


print('the TIME is noon'.capitalize())


# In[32]:


print("wHO writes LIKE tHIS?".swapcase())


# In[33]:


whisper_this = "Can you hear me?"
print(whisper_this.lower())


# In[34]:


yell_this = "Can you hear me Now!?"
print(yell_this.upper())


# In[36]:


format_input = input('enter a string to reformat: ').upper()
print(format_input)


# In[37]:


format_input = input('enter a string to reformat: ').lower()
print(format_input)


# In[38]:



format_input = input('enter a string to reformat: ').swapcase()
print(format_input)


# In[35]:


format_input = input('enter a string to reformat: '.upper())
print(format_input.title())


# In[40]:


hello = input("enter your animal name: ".title())
print('tiger' in hello)


# In[1]:


can_read = input('what is i am reading: ')
can_read_things = ('newspaper,comic,book,panchtantr,mexy,mastram,harry potter and the cursed child')
print(can_read in can_read_things)


# In[1]:


input_test = input('enter something that u are eaten in last 24 hours ')
contain_probs = "cake,milk,dairy,seafood,fish,sweet,chocolate,others"
print(input_test in contain_probs )


# In[1]:


input_test = input('enter something eaten in last 24 hours: ')
contain_probs = 'seafood,dairy,nuts,chocolate'
print(input_test in contain_probs)


# In[6]:


print('hello','world!')
print()
print('welcome','in','the','world','of','lacochick')


# In[15]:


def say_hi():
    print('hello world')
def seex():    
    print('sexy')


# In[16]:


say_hi()


# In[11]:


def hell_3():
    print(33)


# In[12]:


hell_3()


# In[13]:


def hello():
    print()


# In[14]:


hello()


# In[17]:


say_hi()
hello()
seex()
hello()
hell_3()


# In[4]:


def yell_it():
    phrase = 'hello world!'
    print(phrase)


# In[5]:


yell_it()


# In[6]:


def sexy():
    print()
    


# In[27]:


sexy('hello')


# In[12]:


def hell_o(x = 3.14):
    type(x)


# In[10]:


type(hell_o())


# In[15]:


def o_k(phrase = "hello"):
    print(phrase)
    


# In[16]:


o_k()


# In[18]:


o_k('fellow')


# In[1]:


def words_to_yell(phrase = 'sx'):
    print(phrase)
    


# In[2]:


def yell_this():
    print('hello lacocheck')
    


# In[6]:


yell_this(words_to_yell("bend over"))


# In[7]:


words_to_yell()


# In[9]:


def 3_aak():
    print('hello wrld')


# In[19]:


def add_num(num_1 = 10):
    print(num_1 + num_1)    


# In[20]:


add_num()


# In[22]:


def kadu(sex):
    time = sex/sex
    return time
i_want = kadu(100000000000000000000000000000000000000000000000000)
print('i want to do sex with u',i_want,'time')


# In[28]:


def nis(i_hate_u):
    print(i_hate_u)
    i = wants_to_fuck_u
    return i
    


# In[29]:


nis()


# In[31]:


def msg_double(phrase):
    double = phrase + " " + phrase
    return double
print(msg_double('Save Now!'.swapcase()))


# In[1]:


def make_doctor():
    full_name = input('full_input: ')
    return full_name


# In[2]:


make_doctor()


# In[7]:


def aak_rsh():
    type(3.14)


# In[9]:


print(aak_rsh())


# In[20]:


def se_x():
    print()


# In[22]:


print(se_x('hello'),aak_rsh())


# In[12]:


se_x(aak_rsh())


# In[23]:


def sunny(chutiya):
    return 'bavli gand'.title()
    
print(sunny('chutiya'))


# In[5]:


def arti(good = 'sex'):
    return 3.14
type(arti())


# In[16]:


def make_scheduel(preiod1,preiod2):
   return 3.14
print(make_scheduel('math','sst'))


# In[17]:


def make_scheduel(preiod1,preiod2):
   return 'sex'
print(make_scheduel('math','sst'))


# In[24]:


def student_info(name,age,sex):
    return 'student: '.title() + name + '\nage: '.title() + age + '\nsex: '.title() + sex
print(student_info('mukesh'.title(),'18','male'.title()))


# In[25]:


def period_arrange(period1,period2,period3):
    return '1. ' + period1 + '\n2. ' + period2 + '\n3. ' + period3
print(period_arrange('mathematics'.title(),'biology'.title(),'science'.title()))


# In[27]:


def add_num(num_1,num_2 = 10):
    return num_1 + num_2
print(add_num(100))


# In[28]:


first_name = 34


# In[29]:


print(first_name)


# In[30]:


type(first_name)


# In[3]:


def hat_available(color):
    hat_color = 'green,black,red,blue,yellow'
    return color in hat_color


# In[6]:


hat_available('green')


# In[1]:


def fishstore(fish,price):
    return 'Fish type: ' + fish + ' Costs: ' + price
fish = input('Enter Your Fish Name: ')
price = input('enter your price: '.title())


# In[4]:


print(fishstore(fish,price))


# In[1]:


someone_i_know = input()
if someone_i_know:
    print('have u been meet?'.title())
else:
    print('nice to meet u')


# In[7]:


someone_i_know = False
if someone_i_know:
    print('have u been meet?'.title())
else:
    pass


# In[11]:


name = input().title()
someone_i_know = name
if someone_i_know:
    print('have u been meet?'.title())
else:
    print('nice to meet u')


# In[1]:


kadu =input('enter your fav.: '.title())
if kadu.isalpha():
    print('thats goodone')
else:
    print('try next time')


# In[2]:


kadu =input('enter your fav.: '.title())
if kadu.isalnum():
    print('thats goodone')
else:
    print('try next time')


# In[3]:


kadu =input('enter your fav.: '.title())
if kadu.isalpha():
    print('thats goodone')
else:
    print('try next time')


# In[1]:


kadu =input('enter your fav.: '.title())
if kadu.isalnum():
    print('thats goodone')
else:
    print('try next time')


# In[1]:


kadu =input('enter your fav.: '.title()).title()
if kadu.istitle():
    print('thats goodone')
else:
    print('try next time')


# In[2]:


kadu =input('enter your fav.: '.title())
if kadu.istitle():
    print('thats goodone')
else:
    print('try next time')


# In[3]:


kadu =input('enter your fav.: '.title())
if kadu.isdigit():
    print('thats goodone')
else:
    print('try next time')


# In[5]:


kadu =input('enter your fav.: '.title())
if kadu.isdigit():
    print('thats goodone')
else:
    print('try next time')


# In[6]:


kadu =input('enter your fav.: '.title()).upper()
if kadu.isupper():
    print('thats goodone')
else:
    print('try next time')


# In[7]:


kadu =input('enter your fav.: '.title())
if kadu.isupper():
    print('thats goodone')
else:
    print('try next time')


# In[8]:


kadu =input('enter your fav.: '.title())
if kadu.startswith('s'):
    print('thats goodone')
else:
    print('try next time')


# In[9]:


kadu =input('enter your fav.: '.title())
if kadu.startswith('s'):
    print('thats goodone')
else:
    print('try next time')


# In[10]:


kadu =input('enter your fav.: '.title())
if kadu.startswith('s'):
    print('thats goodone')
else:
    print('try next time')
if kadu.isdigit():
    print('have dick')
else:
    print('don"t cry')


# In[11]:


kadu =input('enter your fav.: '.title())
if kadu.startswith('s'):
    print('thats goodone')
else:
    print('try next time')
if kadu.isdigit():
    print('have dick')
else:
    print('don"t cry')


# In[12]:


3>4


# In[13]:


3<4


# In[15]:


3>=2
4<=3


# In[16]:


points = 10
points==19


# In[18]:


points = 10
points==10


# In[19]:


4 != 4


# In[20]:


5 != 6


# In[21]:


someone_i_know = 3>5
if someone_i_know:
    print('have u been meet?'.title())
else:
    print('nice to meet u')


# In[1]:


someone_i_know = input()
if someone_i_know:
    print('have u been meet?'.title())
else:
    print('nice to meet u')


# In[4]:


x = 25

if x > 30:
    x = input('number that u want: '.title())
    print('this is that u want',x)
else:
    print('fuck u')


# In[5]:


x = 25

if x < 30:
    x = input('number that u want: '.title())
    print('this is that u want',x)
else:
    print('fuck u')


# In[6]:


x = 25

if x == 30:
    x = input('number that u want: '.title())
    print('this is that u want',x)
else:
    print('fuck u')


# In[7]:


x = 25

if x != 30:
    x = input('number that u want: '.title())
    print('this is that u want',x)
else:
    print('fuck u')


# In[8]:


ty_pe = input('enter your fav. digit: '.title())
if ty_pe.isdigit():
    print('this is your fav.'.title(),ty_pe)
else:
    pass


# In[10]:


assignment = 25

if assignment:
    print('use "=" to assign values')
else:
    pass


# In[3]:


'aakrsh' == 'aakrsh'


# In[4]:


'kadu' != 'aakrsh'


# In[7]:


'a' > 'A'


# In[8]:


'b' < 'B'


# In[9]:


'AAkrsh' <= 'Kadu'


# In[10]:


'AAkrsh' < 'Kadu'


# In[11]:


'AAkrsh' <= 'Kadu' > 'ravi'


# In[12]:


'Ravi' <= 'Kadu'


# In[13]:


"hello" < "Hello"


# In[14]:


# review and run code
"Aardvark" > "Zebra"
# review and run code
'student' != 'Student'
# review and run code
print("'student' >= 'Student' is", 'student' >= 'Student')
print("'student' != 'Student' is", 'student' != 'Student')
# review and run code
"Hello " + "World!" == "Hello World!"


# In[16]:


msg = 'Save the notebook'
if msg == 'save the notebook':
    print('message as expected')
else:
    print('message as not expected')


# In[17]:


msg = 'Save the notebook'
if msg != 'save the notebook':
    print('message as expected')
else:
    print('message as not expected')


# In[21]:


msg = 'Save the notebook'
preidiction = 'SAVE THE NOTEBOOK'
if msg.upper() == preidiction:
    print('message as expected')
else:
    print('message as not expected')


# In[25]:


alpha = input('input your alphabet: '.title())
vowels = 'a e i o u A E I O U' 
if alpha in vowels:
    print('this is a vowel'.title())
else:
    print('this is a consonant'.title())


# In[27]:


i_name = input('enter your last name: '.title())
cast = 'mahajan rajput brhamin shudr'
if i_name in cast:
    print('u are hindu'.title())
else:
    religon = input('what is your religon: '.title())
    print('so u are a',religon)


# In[28]:


i_name = input('enter your last name: '.title())
cast = 'mahajan rajput brhamin shudr'
if i_name in cast:
    print('u are hindu'.title())
else:
    religon = input('what is your religon: '.title())
    print('so u are a',religon)


# In[1]:


alphabet = input('enter your alphabet: '.title())
if 'a' == alphabet <= 'e':
    print('this is a vowel a or e')
    vowels = 'i o q I O Q'
    if alphabet in vowels:
        print('goodone aakrsh')
    else:
        print('this is a consonant')
else:
    pass


# In[2]:


alphabet = input('enter your alphabet: '.title())
if 'a' == alphabet <= 'e':
    print('this is a vowel a or e')
else:
    vowels = 'i o q I O Q'
    if alphabet in vowels:
        print('goodone aakrsh')
    else:
        print('this is a consonant')


# In[3]:


alphabet = input('enter your alphabet: '.title())
if 'a' == alphabet <= 'e':
    print('this is a vowel a or e')
else:
    vowels = 'i o q I O Q'
    if alphabet in vowels:
        print('goodone aakrsh')
    else:
        print('this is a consonant')


# In[4]:


alphabet = input('enter your alphabet: '.title())
if 'a' == alphabet <= 'e':
    print('this is a vowel a or e')
else:
    vowels = 'i o q I O Q'
    if alphabet in vowels:
        print('goodone aakrsh')
    else:
        print('this is a consonant')


# In[1]:


def tf_quiz(question,answer):
    ty_pe = input(question)
    if ty_pe == True:
        print('correct')
    else:
        print('incorrect')


# In[2]:


quiz_eval = tf_quiz('ouctps have green blood: ','f')
print('your answer is',quiz_eval)


# In[7]:


vissu = input('time that u want to: '.title())
mone_y = input('remaining money'.title())
if vissu == '2' mone_y == '0':
    print('u are my good friend'.title())
elif vissu == '10' mone_y == '0':
    print('bhai paise kb dega mere')
elif vissu == '20' mone_y == '0':
    print('gand mrane gyi dosti')
elif vissu == 'don"t know' mone_y == '0':
    print('ab dekh me teri gand marunga')
else:
    print('intzar kr')


# In[8]:


vissu = input('time that u want to: '.title())
mone_y = input('remaining money'.title())
if vissu == '2' mone_y == '0':
    print('u are my good friend'.title())
elif vissu == '10' mone_y == '0':
    print('bhai paise kb dega mere')
elif vissu == '20' mone_y == '0':
    print('gand mrane gyi dosti')
elif vissu == 'don"t know' mone_y == '0':
    print('ab dekh me teri gand marunga')
else:
    print('intzar kr')


# In[ ]:




