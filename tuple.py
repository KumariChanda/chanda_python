a=(1,2,3,"chanda","kumari","delhi")
print(a)
print(a[0])

print(len(a))
print(a[:3])
print(("delhi" in a))

t=12345,54321,'abcde'
print(t)
#t.append(5555)
print(type(t))
'''un-packing'''
x,y,z=t
print(x)
print(y)
print(z)

'''packing'''
a=1253
b=59868
c='abhhh'
m=a,b,c
print(m)

'''swapping of two number using xor'''
x=5
y=6
x=x^y
y=x^y
x=x^y
print(x,y)

x=5
y=6
x,y=y,x#swapping in python
print(x,y)
