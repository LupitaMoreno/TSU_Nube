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
    
    print(str(a)+ ' '+ op + ' '+str(b)+ ' '+'='+' '+ str(resultado))
    return(resultado)

print('Calculadora ')
# Solicitando la operacion que requiere

solicitud = str(input('Ingresa la operacion que deseas, ej. 3+2*8/2 \n'))

#Extrayendo las operaciones a realizar
ops = []
for op in solicitud:
    if op in lista :
        ops.append(op)

#Creando una lista con la secuencia de operaciones   
sec = []
pos = 0
for ele in ops :
    pos += 1
    #print(ele)
    sec.append(solicitud.split(ele,1)[0])
    sec.append(ele)
    #print(sec)
    solicitud = solicitud.split(ele,1)[1]
    #print(solicitud)
    if pos == len(ops):
        sec.append(solicitud)

#Validando que las operaciones y los datos se ingresen correctamente

# Realizando las operaciones una por una    
i = 0 
res = float(sec[0])
while i+2 <= (len(sec)-1) :
    res = calculadora(res,sec[i+1],float(sec[i+2]))
    i += 2
print('Resultado:', res)