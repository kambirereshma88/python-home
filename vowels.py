
#Write a program that accepts a string from the user and display the same string

#after removing vowels from it.

"""
vowels="aeiouAEIOU"
string=input("Enter a string :")
display=""
i=0
while i < len(string):
    if string[i] not in vowels:
        display+=string[i]
    i+=1
print("string after removing vowels: ",display)
        
"""


vowels="aeiouAEIOU"
string= input("enter a string:")
result=""
i=0
while i<len(string):
    if string[i]not in vowels:
        result+=string[i]
    i+=1
print("string after removing vowels: ",result)
























