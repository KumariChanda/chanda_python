'''looping with list data structure'''
l1=[1,2,3,4]
l2=["a","b","c","d"]
comp=[l1,l2]
print(comp)
print(comp[1][3])
for i in range(len(l1)):
    print(l1[i]," ",l2[i])
    
for i in zip(l1,l2):
    print(i)
