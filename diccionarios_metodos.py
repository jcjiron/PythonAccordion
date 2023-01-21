diccionario = {
    "clave1": 123,
    "clave2": True,
    "clave3": [1,2,3]
}

for key in diccionario.keys():
    print(diccionario[key])

for i,c in diccionario.items():
    print(i,c)