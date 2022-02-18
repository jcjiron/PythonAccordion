
#Sort List Alphanumerically
print("*********************************")
print("Sort List Alphanumerically")
print("*********************************")
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#Sort the list numerically
print("*********************************")
print("Sort the list numerically")
print("*********************************")
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#Sort the list descending
print("*********************************")
print("Sort the list descending")
print("*********************************")
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#Sort the list based on how close the number is to 50
print("*********************************")
print("Sort the list based on how close the number is to 50")
print("*********************************")
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#Reverse the order of the list items
print("*********************************")
print("Reverse the order of the list items")
print("*********************************")
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#Make a copy of a list with the copy() method
print("*********************************")
print("Make a copy of a list with the copy() method")
print("*********************************")
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Make a copy of a list with the list() method
print("*********************************")
print("Make a copy of a list with the list() method")
print("*********************************")
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
















