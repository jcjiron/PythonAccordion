conjunto1 = set({1,2,3,4,5,6,7})
conjunto2 = set({5,6,7,8,9,0})


print(conjunto1)
print(conjunto2)


conjunto1.add(0)
print(conjunto1)

new_set = conjunto1.intersection(conjunto2)

print(new_set)


conjunto1.pop()
print(conjunto1)

conjunto2.remove(5)
print( conjunto2)


