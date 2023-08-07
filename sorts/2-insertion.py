


def sort(items):
    for i in range(0, len(items)):
        j=i
        while j>0 and items[j-1]>items[j]:
            aux = items[j]
            items[j] = items[j-1]
            items[j-1] = aux
            j = j-1
    return items


print("""Complexity O^2""")
print(sort([8,6,5,4,3,2]))