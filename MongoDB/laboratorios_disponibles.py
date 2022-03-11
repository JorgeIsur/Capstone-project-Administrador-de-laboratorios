import pymongo
from termcolor import colored

miCliente = pymongo.MongoClient("mongodb://localhost:27017/")
base_datos = miCliente["Inventario"]
lab_disponibles = base_datos["lab_disponibles"]

global separador
global err_counter
err_counter = 0
separador = "********************************************"

def salir(codigo):
    if codigo==0:
        print(colored("Saliendo..",'green'))
        exit()
    if codigo==1:
        print(colored("Hubo errores.",'red'))
        exit()
    if codigo==2:
        print(colored("Ejecución interrumpida por el usuario.",'yellow'))
        exit()
def registroLaboratorios():
    print(colored(separador,'blue'))
    print(colored("Registro de laboratorios",'yellow',attrs=['bold']))
    print(colored(separador,'blue'))
    nombre_lab = input(colored("Ingresa el laboratorio a registrar:\t",'blue'))
    cupo = input(colored("Ingresa el cupo del laboratorio:\t",'blue'))
    responsable = input(colored("Ingresa el nombre del responsable:\t",'blue'))
    areas = ['CBI','CSH','CBS']
    for i in areas:
        print(colored(f"-{i}",'yellow'))
    area = input(colored("Ingresa el area al que pertenece el laboratorio:\t",'blue'))
    habilitado = input(colored("¿Habilitar el laboratorio ahora?-->Si/No")).lower()
    registro = {"nombre":nombre_lab,"cupo":cupo,"responsable":responsable,"area":area,"habilitado":habilitado}
    try:
        insertar=lab_disponibles.insert_one(registro)
    except Exception as error:
        print(colored(separador,'red'))
        print(colored("Ocurrió un error al insertar el elemento",'red'))
        print(colored(f"error:{error}",'red'))
        print(colored("Intentalo de nuevo.",'yellow'))
        registroLaboratorios()
    print(colored(separador,'green'))
    print(colored("Registro exitoso.",'green'))
    print(colored(separador,'green'))
    print(colored("¿Deseas registrar otro laboratorio?",'blue'))
    eleccion=input(colored("->si/no",'green')).lower()
    if eleccion=='si':
        registroLaboratorios()
    if eleccion=='no':
        menu()
    else:
        print(colored("Opción no soportada,regresando al menú",'red'))
        menu()

def borrarLaboratorios():
    print(colored(separador,'blue'))
    print(colored("Borrado de Laboratorios",'yellow',attrs=['bold']))
    print(colored(separador,'blue'))
    laboratorio=input(colored("Ingresa el laboratorio a borrar:\t",'blue',attrs=['bold']))
    query={"nombre":laboratorio}
    try:
        borrar=lab_disponibles.delete_one(query)
    except Exception as error:
        print(colored(separador,'red'))
        print(colored("Ocurrió un error al borrar el elemento.",'red'))
        print(colored(f"error:{error}",'red'))
        print(colored("Intentalo de nuevo.",'yellow'))
        print(colored(separador,'red'))
        borrarLaboratorios()
    print(colored(separador,'green'))
    print(colored("Borrado exitoso.",'green'))
    print(colored(separador,'green'))
    print(colored("¿Deseas borrar otro laboratorio?",'blue'))
    eleccion=input(colored("->si/no",'green',attrs=['bold'])).lower()
    if eleccion=='si':
        borrarLaboratorios()
    if eleccion=='no':
        menu()
    else:
        print(colored("Opción no soportada, regresando al menú",'red'))
        menu()
def mostrarLaboratorios():
    for data in lab_disponibles.find():
        print(colored(separador,'magenta'))
        print(colored("Nombre:",'blue')+colored(data['nombre'],'green'))
        print(colored("Cupo:",'blue')+colored(data['cupo'],'white'))
        print(colored("Responsable:",'blue')+colored(data['responsable'],'white'))
        print(colored("Area:",'blue')+colored(data['area'],'white'))
        if data['habilitado']=='si':
            print(colored("Habilitado:",'blue')+colored(data['habilitado'],'green'))
        if data['habilitado']=='no':
            print(colored("Habilitado:",'blue')+colored(data['habilitado'],'red'))
        print(colored(separador,'magenta'))
    menu()
def menu():
    print(colored(separador,'blue'))
    print(colored("Menú",'yellow',attrs=['bold']))
    print(colored(separador,'blue'))
    print(colored("""
    1.Registrar un nuevo laboratorio.
    2.Borrar un laboratorio.
    3.Mostrar Laboratorios Existentes.
    4.Salir""",'blue'))
    eleccion=input(colored("Selecciona una opción--->",'green',attrs=['bold']))
    if eleccion=='1':
        registroLaboratorios()
    if eleccion=='2':
        borrarLaboratorios()
    if eleccion=='3':
        mostrarLaboratorios()
    if eleccion=='4':
        salir(0)
    else:
        print(colored("Opción no soportada",'red'))
        menu()
try:
    print(colored(separador,'green'))
    print(colored("Sistema de administración de Laboratorios",'magenta',attrs=['bold']))
    print(colored(separador,'green'))
    menu()
except KeyboardInterrupt:
    print("\n")
    salir(2)