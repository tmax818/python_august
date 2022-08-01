# a function is what it returns!!!!!

# function w/o param

def hello():
    print('whatever')
    return 'something'

print(hello())


# function w/ param

def say_hello(param):
    print(f"hello {param}")

say_hello('nisrine')
# say_hello()


# function w/ default param

def say_hi(name = "programmer"):
    print(f"hello {name}")
    return name

print("first", say_hi())
print("second",say_hi('dashawn'))

def multi(*args):
    print(args)
    for i in args:
        print(i)

def dictmulti(**kwargs):
    print(kwargs)

multi('first', 'second', 'third')

dictmulti(first='tyler', age=39)