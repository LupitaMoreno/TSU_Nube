#Programacion de una calculadora

# Operaciones incluidas
lista = [ '+', '-', '*', '/','^']
# Definiendo la funci'on que realiza las operaciones 
def calculadora(a, op ,b):
    if op == '+':
        resultado =(a+b)
    elif op == '-':
        resultado =(a-b)
    elif op == '*':
        resultado =(a*b)
    elif op == '/':
        resultado =(a/b)
    elif op == '^' :
        resultado =(a**b)
    else :
        resultado = ('algo esta mal')
    resultado = str(a)+ ' '+ op + ' '+str(b)+ ' '+'='+' '+ str(resultado)
    return(print(resultado))


print('Calculadora ')
# Solicitando primera cifra con control de errores
while True:
    try:
        a = float(input('Ingresa la primer cantidad:'))
    except ValueError :
        print('No es un número válido')
    else :
        break


op = '0'
while op not in lista:
    op = str(input('Ingresa el simbolo de la operacion, esta permitido +, -, *, /,^'))
    if op not in lista :
        input('Operacion no valida')


#Solicitando segunda cifra con control de errores
while True:
    try:
        b = float(input('Ingresa la segunda cantidad:'))
    except ValueError :
        print('No es un número válido')
    else :
        break
calculadora(a,op,b)