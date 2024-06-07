file_path="test.txt"

with open ("test.txt","a+") as file:
    file.write("abcde")

with open(file_path,'r')as file:
    first_five_chars = file.read(5)
    print("First 5 characters :", first_five_chars)

with open(file_path,'r') as file:
    content=file.read()
    total_chars=len(content)
    print("Total number of characters :",total_chars)



