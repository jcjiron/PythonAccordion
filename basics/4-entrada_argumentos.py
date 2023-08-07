import sys

if len(sys.argv)==3:
    texto = sys.argv[1]
    repeticiones = int(sys.argv[2])
    for i in range(repeticiones):
        print(texto)
else:
    print('Error introdujo uno (1) o más de (2) argumentos')
    print('Solución: Introduce los argumentos correctamente')
    print('Solución ejemplo: entrad_arguments.py texto  \'texto\' 10')