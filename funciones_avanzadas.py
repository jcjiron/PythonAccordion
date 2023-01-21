edades = [12,11,25,44,6,10,15,16,18,20,26,66,79]

#Filter
def mayores(edad):
    return edad>=18

entrar = list(filter(mayores,edades))
print(entrar)



#lambda
impar = lambda numero: numero%2 !=0
print(impar(20))

doblar = lambda numero: numero*2
print(doblar(4))

#map
print(list(map(doblar, edades)))