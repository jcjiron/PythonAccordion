

#Without list comprehension
print("*********************************")
print("Without list comprehension")
print("*********************************")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)



#With list comprehension
print("*********************************")
print("With list comprehension")
print("*********************************")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)