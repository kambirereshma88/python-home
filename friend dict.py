##Write a program that has the dictionary of your friends’ names as keys and phone
##
##numbers as its values. Print the dictionary in a sorted order. Prompt the user to
##
##enter the name and check if it is present in the dictionary. If the name is not present,
##
##then enter the details in the dictionary.



friends = {'Anju':'9865401234','Shweta':'9865422356', 'Sayali':'9878568765','Saee':'9865424321','Sanjana':'9562365321'}


def print_sorted_dictionary(d):
    for name in sorted(d.keys()):
        print(f'{name}: {d[name]}')

def add_or_check_friend(d):
    name = input("Enter the friend's name: ")
    if name in d:
        print(f"{name} is already in the dictionary with phone number {d[name]}.")
    else:
        phone = input(f"Enter the phone number for {name}: ")
        d[name] = phone
        print(f"Added {name} with phone number {phone} to the dictionary.")


print("Current dictionary of friends (sorted):")
print_sorted_dictionary(friends)

# Check or add a new friend
add_or_check_friend(friends)

print("\nUpdated dictionary of friends (sorted):")
print_sorted_dictionary(friends)
