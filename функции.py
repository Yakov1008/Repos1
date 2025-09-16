#def function():
#    """Это простейшая функция"""
#    pass
#function()

#def y(x):
#    """Эта функция считает значения по формуле 5*x+2"""
#    return 5*x+2
#print(y(0))

def hello(name):
   print(f'Hello {name}!')
surname='Ivanov'
print(f'My surname is {surname}')
print(hello('world'))
help(y)

a=5
b=2
def y(x):
   return x*a+b
print(y(1))

#a=5
#b=2
#def y(x):
#    a=10
#    return x*a+b
#print(y(1))

#a=5
#b=2
#def y(x):
#    global a
#    a=10
#    return x*a+b
#print(y(1))
#print(a)
def y(x,a,b):
    return a*x + b
print(y(0,1,2))

