

a=[153,111,222,264,140,556,333,799,533,428]
even=[]
odd=[]
for i in a:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("even list: ",even)
print("odd list: ",odd)

