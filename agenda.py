import re
import pandas as pd
#Intenté que el dataframe se imprimiera sin la columna de índices para no causar confusión entre el índice y el id pero se necesita formatearlo en html
#import jinja2

#Done Buscar un contacto
#Done Eliminar contacto
#Done Editar un contacto

#Funcion para validar un número telefónico 
def validar_formato_telefonico(telefono):
    regex = r'^\d{3} \d{3} \d{4}$'
    if re.match(regex, telefono):
        return True 
    else :
        return False

#Done. Ingresar multiples contactos hasta que se escriba la cadena 'parar'

# Validacion: 1) contacto repetido, 2) contacto o numero repetido ,

#4) Se debe poder ingresar un contacto completo o una parte

# Funciones que pueden ayudar al debug. 
    #mostrar todos los contactos, 
    #Done. mostrar un subconjunto de contactos, 
    #ordenar contactos, 
    #Done. buscar por diferentes parametros

# Done. Seria buena idea un ID interno ?
def validar_ingreso_telefono() :
    telefono_valido = False
    while telefono_valido == False :
        telefono = input('\nTeléfono a diez dígitos escritos de la siguiente forma: \n3 dígitos espacio tres dígitos espacio 4 dígitos \nEj. 556 293 28974: ')
        tel = str(telefono)
        if validar_formato_telefonico(tel) :
            telefono_valido = True
        else :
            print('Vuelve a ingresar el teléfono con el formato solicitado')
    return(tel)

#Agregar un nuevo contacto
def agregar_info_contacto(id) :
    print('Ingresa los elementos que se van solicitando')
    name = input('Nombre: ')
    last_name = input('Apellidos: ')
    #Validando que el número telefónico cumpla el formato 
    tel = validar_ingreso_telefono()
    e_mail = input('Correo electrónico: ')
    id += 1 
    contacto ={'Id': [id],'Nombre': [name], 'Apellidos': [last_name], 'Teléfono': [tel], 'email': [e_mail]}
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
    print('\nIngresa todos los elementos que tengas sobre tu contacto')
    opcion = 0
    print('Estas son las opciones de búsqueda, podrás usar varias: \n 1) Nombre \n 2) Apellidos\n 3)Teléfono\n 4)Correo electrónico\n 5)No tengo más elementos\n ')
    while   opcion != 5 :
        opcion = int(input('\nIngresa la opción de búsqueda: '))
        #print(opcion)
        if opcion == 1:
            name = input("Nombre: ")
        elif opcion == 2:
            last_name = input("Apellidos:")
        elif opcion == 3:
            tel = validar_ingreso_telefono()
        elif opcion == 4:
            e_mail = input("Correo electrónico:")
        elif opcion == 5:
            print('\nEl elemento que buscas es el siguiente:')
            contacto ={'Id': [id],'Nombre': [name], 'Apellidos': [last_name], 'Teléfono': [tel], 'email': [e_mail]} 
            contacto_a_buscar = []
            for key, value in contacto.items() :
                if key != 'Id' :
                    if value[0] != None :
                        contacto_a_buscar.append(value[0])
                        print(key, ':', value[0])
            return(contacto_a_buscar)
        else:
            print('Escoge una opcion válida')
     
def imprimir_resultado_busqueda(resultado):
    if resultado.empty :
        print('\nNo hay coincidencias con tu búsqueda')
        return()
    else :
        print('\nEl contacto que buscas coincide con los siguientes registros')
        print(resultado)
        return()
# Menu principal    
id = 5    
#agenda = pd.DataFrame(columns = ['Id','Nombre', 'Apellidos', 'Teléfono', 'email'])

data = {
    'Id': [1, 2, 3, 4, 5],
    'Nombre': ['Juan', 'María', 'Pedro', 'Ana', 'Luis'],
    'Apellidos': ['Pérez', 'Gómez', 'López', 'García', 'Martínez'],
    'Teléfono': ['123 456 7890', '234 567 8901', '345 678 9012', '456 789 0123', '567 890 1234'],
    'email': ['juan@example.com', 'maria@example.com', 'pedro@example.com', 'ana@example.com', 'luis@example.com']
}

# Crear el DataFrame
agenda = pd.DataFrame(data)

while True:   
    print('\nAgenda telefónica \n Menú de opciones \n 0)Mostrar la agenda completa \n 1) Agregar un contacto nuevo \n 2) Buscar un contacto\n 3) Eliminar un contacto \n 4) Editar un contacto\n 5) Salir')
    opcion = input('\nElige el número de la opción que desees: ')
    opcion = int(opcion)
    #print(opcion)
    print('\n Elegiste la siguiente acción:')
    if opcion == 0:
        opcion = int(input('\n Mostrar la agenda. Elige la opción que necesites \n1) Completa 2) Por nombre 3) Por Apellido\n'))
        if opcion == 1:
            print(agenda.sort_values('Apellidos'))
        elif opcion == 2:
            name = input('\nEscribe que nombre que estas buscando, puedes ser la inicial (p ej. M) o que contenga una parte (p ej. ana)')
            print(agenda[agenda.Nombre.str.contains(name)])        
        elif opcion == 3:
            last_name = input('\nEscribe que apellido que estas buscando, puedes ser la inicial (p ej. M de Martínez) o que contenga una parte (p ej. nandez)')
            print(agenda[agenda.Apellidos.str.contains(name)])  
        else :
            print('\nElige una opción valida]')
        input('\nDa enter para continuar.')
        
    elif opcion == 1:
        continuar = 'continuar'
        print('\nAgregar contacto nuevo')
        while continuar.lower() != 'parar' :
            contacto , id = agregar_info_contacto(id)
            verificando_telefono = agenda[agenda['Teléfono'] == contacto['Teléfono'][0]]
            verificando_nombre = agenda[(agenda['Nombre'] == contacto['Nombre'][0]) & (agenda['Apellidos'] == contacto['Apellidos'][0])]
            if verificando_nombre.empty and verificando_telefono.empty :
                agenda = pd.concat([agenda,pd.DataFrame(contacto)] ,ignore_index=True)
                print('\nContacto agregado')
                for key, value in contacto.items() :
                    if key != 'Id' :
                        if value[0] != None :
                            print(key, ':', value[0])
            elif not verificando_nombre.empty and not verificando_telefono.empty :
                print('\nExiste al menos un contacto con el mismo número de teléfono, nombre y apellido')
                print(verificando_telefono, '\n', verificando_nombre )
                continuar = input('\nDesea 1) continuar con el registro o 2) Cancelar ')
                if continuar == '1' :
                    agenda = pd.concat([agenda,pd.DataFrame(contacto)] ,ignore_index=True)
                    print('\nContacto agregado')
                    for key, value in contacto.items() :
                        if key != 'Id' :
                            if value[0] != None :
                                print(key, ':', value[0])
                elif continuar == '2' :
                    print('\nCancelando el registro')
            elif not verificando_telefono.empty :
                print('\nExiste al menos un contacto con el mismo número de teléfono')
                print(verificando_telefono)
                continuar = input('\nDesea 1) continuar con el registro o 2) Cancelar ')
                if continuar == '1' :
                    agenda = pd.concat([agenda,pd.DataFrame(contacto)] ,ignore_index=True)
                    print('\nContacto agregado')
                    for key, value in contacto.items() :
                        if key != 'Id' :
                            if value[0] != None :
                                print(key, ':', value[0])
                elif continuar == '2' :
                    print('\nCancelando el registro')
            elif not verificando_nombre.empty :
                print('\nExiste al menos un contacto con el mismo nombre y apellido')
                print(verificando_telefono)
                continuar = input('\nDesea 1) continuar con el registro o 2) Cancelar ')
                if continuar == '1' :
                    agenda = pd.concat([agenda,pd.DataFrame(contacto)] ,ignore_index=True)
                    print('\nContacto agregado')
                    for key, value in contacto.items() :
                        if key != 'Id' :
                            if value[0] != None :
                                print(key, ':', value[0])
                elif continuar == '2' :
                    print('\nCancelando el registro')

            continuar = input('\nEscribe "parar" si ya no quieres agregar otro contacto de otro modo escribe c de continuar: ')
    elif opcion == 2:
        print("\nBuscar un contacto")
        contacto_a_buscar = agregar_info_busqueda()       
        resultado = agenda.iloc[agenda[agenda.isin(contacto_a_buscar)].dropna(how = 'all').index]
        imprimir_resultado_busqueda(resultado)
        input('\nDa enter para continuar al menú principal. ')
    elif opcion == 3:
        print("\nEliminar un contacto")
        contacto_a_buscar = agregar_info_busqueda()
        resultado = agenda.iloc[agenda[agenda.isin(contacto_a_buscar)].dropna(how = 'all').index]
        imprimir_resultado_busqueda(resultado)
        id_busqueda = int(input('\nElige el id del contacto que deseas eliminar: '))
        print('\nElegiste el siguiente registro')
        print(agenda[agenda['Id'] == id_busqueda])
        confirmacion = input('\nConfirmas que deseas elimnar este contacto (sí, no): ')
        if confirmacion.lower() in ['si','sí'] :
            agenda.drop(agenda[agenda['Id'] == id_busqueda].index, inplace=True)
            print('\nEl contacto fue eliminado')
        else :
            print('\nNo se elimnó el contacto')
        input('\nDa enter para continuar al menú principal')
    elif opcion == 4:
        print("\nEditar un contacto")
        contacto_a_buscar = agregar_info_busqueda()
        resultado = agenda.iloc[agenda[agenda.isin(contacto_a_buscar)].dropna(how = 'all').index]
        imprimir_resultado_busqueda(resultado)
        id_busqueda = int(input('\nElige el id del contacto que deseas editar: '))
        print('\nElegiste el siguiente registro')
        print('\n',agenda[agenda['Id'] == id_busqueda])
        confirmacion = input('\nConfirmas que desas editar (si, no): ')
        if confirmacion.lower() in ['si','sí'] :
            opcion = 0
            print('Opciones que se pueden editar: \n 1) Nombre \n 2) Apellidos\n 3)Teléfono\n 4)Correo electrónico\n 5)No deseo editar más opciones \n ')
            while   opcion != 5 :
                opcion = int(input('\nIngresa la opción que deseas editar: '))
                #print(opcion)
                if opcion == 1:
                    name = input("Nombre:")
                    agenda.loc[agenda['Id'] == id_busqueda,'Nombre'] = name
                elif opcion == 2:
                    last_name = input("Apellidos:")
                    agenda.loc[agenda['Id'] == id_busqueda,'Apellidos'] = last_name
                elif opcion == 3:
                    tel = validar_ingreso_telefono()

                    agenda.loc[agenda['Id'] == id_busqueda,'Teléfono'] = tel
                elif opcion == 4:
                    e_mail = input("Correo electrónico:")
                    agenda.loc[agenda['Id'] == id_busqueda,'email'] = e_mail
                elif opcion == 5:
                    print('Saldrás del ambiente de edición')
                else :
                    print('\nIngresar una opción que se encuentre en el menú.')
            print('\nEl contacto queda registrado de la siguiente forma: ')
            print('\n',agenda[agenda['Id'] == id_busqueda])   
            input('\n Da enter para continuar')
        else :
            print('\nSaldrás del ambiente de edición')

    elif opcion == 5:
        print("\nCerrar la agenda\n")
        break  
    else:
        print('\nElige una opcion que se encuentre en el menú')



