import re
import pandas as pd

#Buscar un contacto
#Eliminar contacto
#Editar un contacto

#Funcion para validar un numero teléfonico 
def validar_numero_telefonico(telefono):
    regex = r'^\d{3} \d{3} \d{4}$'
    if re.match(regex, telefono):
        return True 
    else :
        return False
#Done. Ingresar multiples contactos hasta que se escriba la cadena 'parar'

# Validacion: 1) contacto repetido, 2) contacto o numero repetido ,

#4) Se debe poder ingresar un contacto completo o una parte

# Funciones que pueden ayudar al debug. mostrar todos los contactos, mostrar un subconjunto de contactos, ordenar contactos, buscar por diferentes parametros

# Done. Seria buena idea un ID interno ?

#Agregar un nuevo contacto
def agregar_info_contacto(id) :
    print('Ingresa los elementos que se van solicitando')
    nombre = input('Nombre: ')
    name = nombre
    apellido = input('Apellido: ')
    last_name = apellido
    #Validando que el número telefónico cumpla el formato 
    telefono_valido = False
    while telefono_valido == False :
        telefono = input('Teléfono a diez dígitos escritos de la siguiente forma: 3 dígitos espacio tres dígitos espacio 4 dígitos Ej. 556 293 28974: ')
        tel = str(telefono)
        if validar_numero_telefonico(tel) :
            telefono_valido = True
        else :
            print('Vuelve a ingresar el teléfono con el formato solicitado')

    correo = input('Correo electrónico: ')
    e_mail = correo
    id += 1 
    contacto ={'Id': [id],'Nombre': [name], 'Apellido': [last_name], 'Teléfono': [tel], 'email': [e_mail]}
    #print(pd.DataFrame(contacto))
    return(contacto, id)
#Recopilar información de búsqueda
def agregar_info_busqueda() :
#Intento fallido de asignar valores nan a las variables a traves de su nombre iterando en una lista
#for a in contacto_list :
#    print(a)
#    a = None

    id = None
    name = None
    last_name  = None
    tel = None
    e_mail = None
    print('Entre mas elementos ingreses, tu busqueda será más precisa')
    opcion = 0
    while   opcion != 5 :
        opcion = int(input('Ingresa el número que indique el elemento por el cual quieres buscar \n 1) Nombre \n 2) Apellido\n 3)Teléfono\n 4)Correo electrónico\n 5)No tengo más elementos '))
        #print(opcion)
        if opcion == 1:
            name = input("Nombre:")
        elif opcion == 2:
            last_name = input("Apellido:")
        elif opcion == 3:
            tel = input("Teléfono:")
        elif opcion == 4:
            e_mail = input("Correo electrónico:")
        elif opcion == 5:
            print('El elemento que buscas es el siguiente:')
            contacto ={'Id': [id],'Nombre': [name], 'Apellido': [last_name], 'Teléfono': [tel], 'email': [e_mail]} 
            contacto_a_buscar = []
            for key, value in contacto.items() :
                if key != 'Id' :
                    if value[0] != None :
                        contacto_a_buscar.append(value[0])
                        print(key, ':', value[0])
            return(contacto_a_buscar)
        else:
            print('Escoge una opcion válida')
     

id = 0    
agenda = pd.DataFrame(columns = ['Id','Nombre', 'Apellido', 'Teléfono', 'email'])
# Menu principal
while True:   
    print('Agenda telefónica \n Menú de opciones \n 1) Agregar un contacto nuevo \n 2) Buscar un contacto\n 3) Eliminar un contacto \n 4) Editar un contacto\n 5) Salir')
    opcion = input('Elige el número de la opción que desees: ')
    opcion = int(opcion)
    #print(opcion)
    print('Elegiste la siguiente acción:')
    if opcion == 1:
        continuar = 'continuar'
        print('Agregar contacto nuevo')
        while continuar.lower() != 'parar' :
            contacto , id = agregar_info_contacto(id)
            agenda = pd.concat([agenda,pd.DataFrame(contacto)] ,ignore_index=True)
            print('Contacto agregado')
            for key, value in contacto.items() :
                if key != 'Id' :
                    if value[0] != None :
                        print(key, ':', value[0])
            continuar = input('Escribe "parar" si ya no quieres agregar otro contacto de otro modo escribe c de continuar: ')
    elif opcion == 2:
        print("Buscar un contacto")
        contacto_a_buscar = agregar_info_busqueda()
        
        resultado = agenda.iloc[agenda[agenda.isin(contacto_a_buscar)].dropna(how = 'all').index]
        if resultado.empty :
            print('No hay coincidencias con tu búsqueda')
        else :
            print('El contacto que buscas coincide con los siguientes registros')
            print(resultado)
            input('Da enter para continuar al menú principal')
    elif opcion == 3:
        print("Eliminar un contacto")
    elif opcion == 4:
        print("Editar un contacto")
    elif opcion == 5:
        print("Cerrar la agenda")
        break  
    else:
        print('Elige una opcion que se encuentre en el menú')



