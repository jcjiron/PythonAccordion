"""
* List
"""
print("*********************************")
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#List constructor

print("*********************************")
print("Constructor")
print("*********************************")
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

print("*********************************")
print("Access items")
print("*********************************")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1])
print(thislist[-1])
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])

#Check if Item Exists
print("*********************************")
print("Check if Item Exists")
print("*********************************")
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")



#Insert Items
print("*********************************")
print("Insert Items")
print("*********************************")
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


#Extend List
print("*********************************")
print("Extend List")
print("*********************************")
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


#Add Any Iterable
print("*********************************")
print("Extend List")
print("*********************************")
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


#Remove Specified Item
print("*********************************")
print("Remove Specified Item")
print("*********************************")
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Remove Specified Index
print("*********************************")
print("Remove Specified Index")
print("*********************************")
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#Remove the last item
print("*********************************")
print("Remove the last item")
print("*********************************")
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#Delete the entire list
print("*********************************")
print("Delete the entire list")
print("*********************************")
thislist = ["apple", "banana", "cherry"]
del thislist

#Clear the list content
print("*********************************")
print("Clear the list content:")
print("*********************************")
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#Print all items by referring to their index number
print("*********************************")
print("Print all items by referring to their index number")
print("*********************************")
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#Print all items, using a while loop to go through all the index numbers
print("*********************************")
print("Print all items, using a while loop to go through all the index numbers")
print("*********************************")
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#Print all items, using a while loop to go through all the index numbers
print("*********************************")
print("A short hand for loop that will print all items in a list")
print("*********************************")
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]