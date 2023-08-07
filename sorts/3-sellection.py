

def sort(items):
    for j in range(0,len(items)):
        iMin=j
        for i in range(j+1, len(items)):
            if items[i] < items[iMin]:
                iMin=i
        if iMin != j:
            aux = items[j]
            items[j]= items[iMin]
            items[iMin]=aux
    return items

print("""Complexity O^2 """)
print(sort([7,6,5,4,3,2,1]))