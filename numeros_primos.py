#Dado un intervalo  se arrojara una lista de los números  primos contenidos en el intervalo.

#Funcion que define si es un numero primo


def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            #print("No es primo", n, "es divisor")
            return False
    #print("Es primo")
    return True
        
dato = input('Ingresa un intervalo separado por coma ej.: a,b: ')

a = dato.split(',')
#print(a)

lista = []
for i in range(int(a[0]),int(a[1])):
	if es_primo(i):
		lista.append(i)
print('Los números primos dentro ese intervalo son : ')
print(lista)