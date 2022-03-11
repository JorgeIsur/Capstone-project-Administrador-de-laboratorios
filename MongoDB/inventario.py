import pymongo
import termcolor

miCliente = pymongo.MongoClient("mongodb://localhost:27017/")
base_datos = miCliente["Inventario"]
lab_disponibles = base_datos["lab_disponibles"]

global separador
global laboratorio
global err_counter
separador = "********************************************"

def salir(codigo):
    if codigo==0:
        termcolor.cprint("Saliendo..",'green')
        exit()
    if codigo==1:
        termcolor.cprint("Ejecución interrumpida por el usuario.",'yellow')
        exit()
def registroElemento(laboratorio,laboratorio_nombre):
    print(separador)
    print(f"Registro de elementos en laboratorio {laboratorio_nombre}")
    print(separador)
    nombre_elemento = input("Ingresa el nombre del artículo-->")
    num_inventario = input("Ingresa el número de inventario-->")
    descripcion = input("Ingresa la descripción del artículo-->")
    registro = {"nombre":nombre_elemento,"num_inventario":num_inventario,"descripcion":descripcion,"disponibilidad":"stock"}
    try:
        insertar = laboratorio.insert_one(registro)
    except Exception as e:
        termcolor.cprint(separador,'red')
        termcolor.cprint("Ocurrió un error al insertar el elemento.",'red',attrs=['bold'])
        termcolor.cprint(f"Error:{e}",'red')
        termcolor.cprint("Intentalo de nuevo.",'yellow')
        termcolor.cprint(separador,'red')
        registroElemento(laboratorio)
    termcolor.cprint(separador,'green')
    termcolor.cprint("Registro exitoso",'green',attrs=['bold'])
    termcolor.cprint(separador,'green')
    menu(laboratorio,laboratorio_nombre)
def borrarElemento(laboratorio,laboratorio_nombre):
    termcolor.cprint(separador,'blue')
    termcolor.cprint(f"Borrar elemento en laboratorio {laboratorio_nombre}",'yellow')
    termcolor.cprint(separador,'blue')
    num_inventario = input("Ingresa el número de inventario del artículo a borrar--->")
    query = {"num_inventario":num_inventario}
    try:
        borrar = laboratorio.delete_one(query)
    except Exception as e:
        termcolor.cprint(separador,'red')
        termcolor.cprint("Ocurrió un error al borrar el elemento.",'red',attrs=['bold'])
        termcolor.cprint(f"Error:{e}",'red')
        termcolor.cprint("Intentalo de nuevo.",'yellow')
        termcolor.cprint(separador,'red')
        borrarElemento(laboratorio,laboratorio_nombre)
    termcolor.cprint(separador,"green")
    termcolor.cprint(f"{borrar.deleted_count} elementos borrados.",'green',attrs=['bold'])
    termcolor.cprint("Borrado exitoso.",'green',attrs=['bold'])
    termcolor.cprint(separador,'green')
    menu(laboratorio,laboratorio_nombre)
def imprimirDatabase(laboratorio,laboratorio_nombre):
    print(separador)
    print(laboratorio_nombre)
    print(separador)
    for data in laboratorio.find():
        termcolor.cprint(separador,'magenta')
        print(f"Nombre:{data['nombre']}")
        print(f"Número de inventario:{data['num_inventario']}")
        print(f"Descripción:{data['descripcion']}")
        termcolor.cprint(separador,'magenta')
    menu(laboratorio,laboratorio_nombre)
def menu(laboratorio,laboratorio_nombre):
    termcolor.cprint(separador,'blue')
    termcolor.cprint("MENU","yelow",attrs=['bold'])
    termcolor.cprint(f"Laboratorio {laboratorio_nombre}",'green',attrs=['bold'])
    termcolor.cprint(separador,'blue')
    termcolor.cprint("""
    1.Registrar nuevo elemento
    2.Borrar elemento existente
    3.Mostrar elementos existentes
    4.Salir
    """,'blue')
    eleccion = input(termcolor.colored("Ingresa la opción--->",'green',attrs=['bold']))
    if eleccion == '1':
        registroElemento(laboratorio,laboratorio_nombre)
    if eleccion == '2':
        borrarElemento(laboratorio,laboratorio_nombre)
    if eleccion == '3':
        imprimirDatabase(laboratorio,laboratorio_nombre)
    if eleccion == '4':
        salir(0)
def defineLab(laboratorio):
    laboratorio_col = base_datos[laboratorio]
    return laboratorio_col

try:
    termcolor.cprint(separador,'green')
    termcolor.cprint("Sistema de administración de inventario",'magenta',attrs=['bold'])
    termcolor.cprint(separador,'green')
    termcolor.cprint("Laboratorios disponibles",'yellow')
    for data in lab_disponibles.find():
        termcolor.cprint(f"*{data['nombre']}",'blue')
    laboratorio_nombre = input(termcolor.colored("Ingresa el laboratorio a administrar-->",'green',attrs=['bold'])).upper()
    laboratorio_col = defineLab(laboratorio_nombre)
    menu(laboratorio_col,laboratorio_nombre)
except KeyboardInterrupt:
    print("\n")
    salir(1)

