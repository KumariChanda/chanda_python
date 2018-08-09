age=5
if age>=18:
    print("elligible for voting")
else:
    print("not-elligible")

'''else if'''
marks=58
if marks>=90:
    print("A")
elif marks>=80 and marks<90:
    print("B")
elif marks>=70 and marks<80:
    print("C")
else:
    print("D")

'''palindrome of string'''
word=input("Please enter a word ")
reversed_word=word[::-1]
if word==reversed_word:
    print("palindrome")
else:
    print("Not-palindrome")

''''''
print(bool(None))
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(' '))
print(bool([]))
data=[]
if data:
    print(process(data))
else:
    print("There is no data")
    

