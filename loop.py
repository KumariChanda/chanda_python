# range is use to iterate over a sequence of number
print(range(3))
print(range(5,10))
print(range(2,12,3))
print(range(-7,-30,-5))

for i in range(1,10):
    print(i)

print("************************************")
for j in range(5,10):
    print(j)

print("************************************")
for i in range(2,12,3):
    print(i)
print("************************************")
for i in range(-7,-30,-5):
    print(i)

print("**************************************")

'''break and continue'''
for n in range(10):
    if n==6:
        break
    print(n)
print("**************************************")
for n in range(10):
    if n==6:
        continue
    print(n)
