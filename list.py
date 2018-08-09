'''easy_as=[1,2,3]
print(easy_as)'''
empty=[]
letters=['a','b','c','d','e']
numbers=[2,3,4,5]
print(empty)
print(letters)
print(numbers)
numbers.append(20)#adding an extra element into previous list
print(numbers)

print(numbers[1])#accessing via index of list element

'''appling slice operation like string'''
print(letters[:3])
print(numbers[1:-1])

'''nested list'''
A=[1,2,3,4,5]
B=['a','b','c','d']
C=[A,B]
print(A)
print(B)
print(C)
'''accessing data elements of nested list'''
print(C[0])
print(C[0][2])
print(C[1][2:])


