p = 'who cares?'
def q():
    global p
    print p
    p = 'hello world'
    print(p)
print(q())






aman = 'p'
var = 'global'
def fn1():
    print(aman)
def fn2():
    aman = 'pappu'
    print(aman)
def fn3():
    global var,aman
    print(var)
    var = aman
    print(var)
def fn4():
    aman = 'what to do'
    print(aman)

print aman
print var

fn1()

print aman
print var

fn2()

print aman
print var


fn3()

print aman
print var


fn4()

print aman
print var
