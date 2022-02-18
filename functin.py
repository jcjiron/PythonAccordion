#Basic function
print("*********************************")
print("Basic function")
print("*********************************")
def my_function():
  print("Hello from a function")

my_function()

#Function arguments
print("*********************************")
print("Function arguments")
print("*********************************")
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#Function unknown arguments
print("*********************************")
print("Function unknown arguments")
print("*********************************")
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#Default argument
print("*********************************")
print("Default argument")
print("*********************************")
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


#Basic lambda
print("*********************************")
print("Basic lambda")
print("*********************************")
x = lambda a : a + 10
print(x(5))








