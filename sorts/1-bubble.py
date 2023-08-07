


def sort(items):
    n = len(items)
    for i in range(0, n):
        for j in range(0, n - 1):
            if items[j] > items[j+1]:
                aux = items[j]
                items[j] = items[j+1]
                items[j+1] = aux
    return items
        

print(""" Complecity O^2 """)
print(sort([6,5,4,3,2,1]))