#List
'''roll_no=[]
for i in range(1,60):
    roll_no.append(i)

print(roll_no)

roll_no=[20,14,13,12,11,1,2,3,4,5,6,7,8,9,10]
seating=sorted(roll_no)#to sort list elements.
print(seating)
'''
#DictionaryDS
empty={}
print(type(empty))
print(empty==dict())

a=dict(one=1,two=2,three=3)
b={"one":1,"two":2,"three":3}
print(a==b)


info={"name":'Chanda',"Reg_No":11706374,"Contact":8559080443,"Department":'SCA'}
print(info)
print(info['name'])
info['strength']="lazy"
print(info)

info['marks']=[45,55,65]#dict using list
print(info)
'''dict funtions'''
print(info.get("marks"))#use get() method to avoid key error.

marks=info.get('Marks',[])
print(len(marks))
'''Delete an element from dict'''
del info['Contact']#1
print(info)
info.pop("name")#2
print(info)
#info.popitems("name")#delete the last element from dict
#print(info)
print(info.keys())#display all the keys
print(info.values()) #display all the values 
print(info.items())#display key valye pair

print(len(info.keys()))

print(('Reg_No',11706374) in info.items())#to check whether the given pair is present or not in dict

for values in info.values():
    print(values)

ch=info.copy()#copy the dict
print(ch)

