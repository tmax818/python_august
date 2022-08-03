
# ! data types

print(type('string'))
print(type(42))
print(type(3.14))
print(type(True))
print(type(None))

# ! conditionals and loops

if True:
    print('this ran')

if False:
    print("this didn't run")
start = 0
stop = 10
step = 1
for i in range(start, stop, step):
    print(i)

# ! data structures

## ! dicts

person = {'name': 'Tyler', 'age': 39}
print(person['name'])

my_list = ['apples', 'strawberries', 'pineapple']

my_tuple = ('tyler', 39, True)

# ! functions

def hello():
    print("hello")
    return "hello"

def say_hello(name):
    print(f"Hello {name * 35}")


say_hello("42")
# name = 42
