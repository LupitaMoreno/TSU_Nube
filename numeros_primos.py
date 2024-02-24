#Dado un intervalo  se arrojara una lista de los números  primos contenidos en el intervalo.

#Funcion que define si es un numero primo
import time
inicio = time.time()
def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            #print("No es primo", n, "es divisor")
            return False
    #print("Es primo")
    return True
#Se solicita al usuario ingresar el intervalo de interes y se almacena como un dato tipo string        
dato = input('Ingresa un intervalo separado por coma ej.: a,b: ')
#Se separa el ingreso del usuario en una lista recordando que es tipo string
a = dato.split(',')
#print(a)
#Se crea una lista donde se almacenarán los números primos encontrados
#lista = []
#Se crea un ciclo que va del inicio del intervalo hasta el final, checando si cada número es primo.
#Si es primo se almacena en la lista
#for i in range(int(a[0]),int(a[1])):
#	if es_primo(i):
#		lista.append(i)
#Ahora usando 'list comprehension'            
lista = [i for i in range(int(a[0]),int(a[1])) if es_primo(i)]
#Se reporta la lista de números primos encontrados en el intervalo
print('Los números primos dentro ese intervalo son : ')
print(lista)

fin= time.time()
print('Tiempo de procesamiento: ', '{:.2f}'.format(fin-inicio))