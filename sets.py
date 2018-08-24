s={"C","H","A","N","D","A"}
print(type(s))
print(s)
a=set([1,5,9,4,3,2])
print(type(a))
print(a)
print("A" is a)
s.discard('A')#discard the elements of set same as remove except no error
print(s)
s.add("X")#add new elements in set
print(s)
s.remove("A")#raises KeyError if "A" is not present and remove an element from set
print(s)
a=set("abdefghijklmn")
b=set("alamansovita")
print(a)
print(b)
print(a-b)#set differenece
print(a|b)#union
print(a&b)#intersection
print(a^b)#symmetric difference(a-b union b-a)
