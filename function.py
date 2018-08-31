
'''function without an argument and without return type'''
def cube():
    n=5**3
    print(n)

cube()


'''function with an argument and return type'''
def cube(x):
    return x**3 #Return the cube of number passed to function

n=cube(5)
print(n)

def add(n1,n2):
    """retrun the addtion of numbers passed to function"""
    return(n1+n2) 

print(add(5,6))

'''returning tuple'''
def return_tuple(v1,v2):
    """Raise v1 to the power of v2 and vica versa."""
    nv1=v1**v2
    nv2=v2**v1
    return (nv1,nv2)

result=return_tuple(2,3)
print(result)
print(type(result))
'''
n=10
def scope():
    op=n**2
    return op

print(scope())
print(n)

n=20
print(scope())
print(n)
'''

def scope():
    global n
    n=20
    op=n**2
    return op

print(scope())
print(n)

n=20
print(scope())
print(n)





'''nested function'''
def outer():
    m=5
    print(m)
    def inner():
        print("I'm inner")        

    inner()
    
outer()


def raise_val(n):
    """Return the inner function."""
    def inner(x):
        """Raise x to the power of n."""
        raised=x**n
        return raised
    def inner2(x):
        """Raise x to the power of n."""
        raised=x**n
        return raised
    return inner,inner2

sq,sq1=raise_val(2)

print(sq(2),sq(3))


'''Adding Default Argument'''
def power(n,p=1):
    return(n**p)
print(power(2))
print(power(2,3))
