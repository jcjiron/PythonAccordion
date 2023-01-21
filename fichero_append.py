from io import open


fichero = open("archivo.txt","a")
fichero.write("\n Esto es el metodo append")
fichero.close()
print(fichero)