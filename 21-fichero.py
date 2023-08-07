from io import open

fichero = open("archivo.txt", "w")
texto = "Hola Mundo\nEstudio Python"
fichero.write(texto)
fichero.close()