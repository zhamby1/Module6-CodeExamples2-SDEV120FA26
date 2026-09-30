#to search an array/list we are going to use the in operator in python.
#the in operator is actually looping through the list for us to grab something out of it.

party_invitees = ["Zach","Aly","Tim","Jenny"]

#we can ask the user to see if someone is on the invitee list
find_name = input("Please give me a name you wish to find on the list ")

#if we find the name we can display name found
if find_name in party_invitees:
    print("Found")
    #we can also do a search and replace if we use the .index() function and our search term to find the index of our found value
    found_name_index = party_invitees.index(find_name)

    #we can use the index value to grab whatever name out of the list and modify it if we want to
    party_invitees[found_name_index] = input("Type in the name you want to change this to ")

else:
    print("Person not found.  Check you spelling")


for name in party_invitees:
    print(name)