#import math 
#Solicitando al usuario el tamaño del rombo
lineas = input('Ingresa el número de líneas del rombo, debe ser un número impar.\n')
lineas = int(lineas)
lineas = int((lineas - 1)/2 + 1)
#Primero se hace el triángulo superior
espacios = lineas-1
i=1
j=1
while i<=lineas:
	print(' ' * espacios + '*' * j)
	j=j+2
	espacios= espacios -1
	i=i+1
j=j-2
espacios= espacios +1
#Despues se hace el triángulo inferior
while j>1:
	j=j-2
	espacios= espacios +1
	print(' ' * espacios+'*' * j)