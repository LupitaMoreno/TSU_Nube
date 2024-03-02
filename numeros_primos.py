#Dado un intervalo  se arrojara una lista de los números  primos contenidos en el intervalo.

#Funcion que define si es un numero primo
import time
inicio = time.time()
#Función que devuelve True si es número primo y False si no lo es. También imprime cuando es número primo
def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            #print("No es primo", n, "es divisor")
            return False
    print(num)
    return True
#Se solicita al usuario ingresar el intervalo de interes y se almacena como un dato tipo string        
dato = input('Ingresa un intervalo separado por coma ej.: a,b: ')
a = dato.split(',')
#Ahora usando 'list comprehension'  
print('Los números primos dentro ese intervalo son : ')          
lista = [i for i in range(int(a[0]),int(a[1])) if es_primo(i)]
#Se reporta la lista de números primos encontrados en el intervalo
#print(lista)
# Calcula el timempo de ejecución del programa
fin= time.time()
print('Tiempo de procesamiento: ', '{:.2f}'.format(fin-inicio))