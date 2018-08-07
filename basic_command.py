Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Inte
l)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> type(1)
<class 'int'>
>>> type(None)
<class 'NoneType'>
>>> type(None)
<class 'NoneType'>
>>> type(type(int))
<class 'type'>
>>> +
  File "<stdin>", line 1
    +
    ^
SyntaxError: invalid syntax
>>> 1+1
2
>>> 7-1
6
>>> 10*2
20
>>> 9/3
3.0
>>> 3/2
1.5
>>> 5/2
2.5
>>> 7/1.4
5.0
>>> 9/3
3.0
>>> 9//3
3
>>> 2**3
8
>>> True
True
>>> False
False
>>> False=True
  File "<stdin>", line 1
SyntaxError: can't assign to keyword
>>> True=True
  File "<stdin>", line 1
SyntaxError: can't assign to keyword
>>> not True
False
>>> True and False
False
>>> True or False
True
>>> ==1
  File "<stdin>", line 1
    ==1
     ^
SyntaxError: invalid syntax
>>> 1==1
True
>>> 2*3==5
False
>>> 1!=1
False
>>> 2*3!=5
True
>>> 1<10
True
>>> 2>=0
True
>>> 1<2<3
True
>>> 1<2>=3
False
>>> str1="Chanda"
>>> str2='''kumari'''
>>> str1+str2
'Chandakumari'
>>> str1+" "+str2
'Chanda kumari'
>>> str1
'Chanda'
>>> str[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'type' object is not subscriptable
>>> str1[0]
'C'
>>> str1[1]
'h'
>>> str1[2]
'a'
>>> str1[3]
'n'
>>> str1[4]
'd'
>>> str1[5]
'a'
>>> str1[6]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> str[-6]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'type' object is not subscriptable
>>> str[-1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'type' object is not subscriptable
>>> str1[-6]
'C'
>>> str1[-5]
'h'
>>> str1[-4]
'a'
>>> str1[-3]
'n'
>>> str1[-2]
'd'
>>> str1[-1]
'a'
>>>str1[0:2] 
'Ch'
>>>str1[:6] 
'Chanda'
>>>str1[5:] 
'a'