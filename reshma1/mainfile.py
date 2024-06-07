
with open("C:/Users/rahul/Desktop/python home work/reshma1/source.txt",'r') as source_file:
    content=source_file.read()

with open("C:/Users/rahul/Desktop/python home work/reshma1/destination.txt",'w') as destination_file:
    destination_file.write(content)

print("copied successfully")