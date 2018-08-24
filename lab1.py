Name="Chanda Kumari Singh"
First_Name="Chanda "
Middle_Name="Kumari "
Last_Name="Singh"
print(First_Name+Middle_Name+Last_Name)#concatenation of First Name, Middle Name and Last Name
print(Name[::-1])#Reverse the string
print(Name[:3])#Slice first three charcter of my Name
print(Name[-3:])#Slice first three charcter from oppsite direction
'''appling in-build function of string'''
print(Name.upper())#convert string into upper case
print(Name.lower())#convert the string into lower case
print(Name.title())#convert first letter of each word capital
print(Name.split())#it will split each word of string
print(Name.strip('gh'))#it will discard the entered substring from your string at the last basically remove whitespace from the beginnig and end
print(Name.capitalize())#make first letter of string capital
print(len(Name))#find the length of string
print(Name.replace('a','*'))#it will replace a sbtring from another substring
print(Name.find('n'))#find the number of occurance of substring in string
