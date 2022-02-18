#Basic tupple
print("*********************************")
print("Basic tupple")
print("*********************************")
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Tupple with repeated items
print("*********************************")
print("Tupple with repeated items")
print("*********************************")
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))



#One item tuple, remember the comma:
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


#Using the tuple() method to make a tuple
print("*********************************")
print("Using the tuple() method to make a tuple")
print("*********************************")
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#Convert the tuple into a list to be able to change it
print("*********************************")
print("Convert the tuple into a list to be able to change it")
print("*********************************")
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


#Unpacking a tuple
print("*********************************")
print("Unpacking a tuple")
print("*********************************")
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)








