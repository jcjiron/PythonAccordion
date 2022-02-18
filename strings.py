
import random
print "Hola mundo"


"""
* Str
"""
print "============================================================"
print "Working with strings"
print "============================================================"

name = "juan Carlos Jiron Juarez"
first_name, last_name = "juan", "Jiron Juarez"
age = 27

print name.capitalize()
print ("len(name):"  + str(len(name)))
print ("String as array:")
for x in first_name:
    print x

if first_name in name:
    print "Yes" + first_name + " is in " + name


print ("Juan Carlos, I'm {} years old".format(age))
