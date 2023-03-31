# Turno 4 - Enunciado 2 (T4E2) (Copie el enunciado siguiente como comentario al inicio de su archivo principal de código fuente)
#
# Una empresa de venta de artículos de pesca deportiva mantiene información sobre los distintos artículos que tiene a la venta.
# Por cada artículo se registran los datos siguientes: número de identificación (un entero), descripción del artículo (una cadena),
# precio de venta, lugar de origen del artículo (un valor entre 0 y 24 incluidos, por ejemplo: 0: Argentina, 1: Canadá, etc.)
# y tipo de artículo (un número entero entre 0 y 29 incluidos, para indicar (por ejemplo): 0: anzuelo, 1: caña, etc.)
# Se pide definir un tipo registro Articulo con los campos que se indicaron, y un programa completo con menú de opciones
# para hacer lo siguiente:
#
# 1- Cargar los datos de n registros de tipo Articulo en un arreglo de registros (cargue n por teclado).
# Valide los campos que sea necesario. Puede hacer la carga en forma manual,
# o puede generar los datos en forma automática (con valores aleatorios)
# (pero si hace carga manual, TODA la carga debe ser manual, y si la hace automática entonces TODA debe ser automática).
# El arreglo debe crearse de forma que siempre quede ordenado de menor a mayor, según el número de identificación de los artículos,
# y para hacer esto debe aplicar el algoritmo de inserción ordenada con búsqueda binaria.
# Se considerará directamente incorrecta la solución basada en cargar el arreglo completo y ordenarlo al final,
# o aplicar el algoritmo de inserción ordenada pero con búsqueda secuencial.
#
# 2- Mostrar el arreglo creado en el punto 1, a razón de  un registro por línea.
# Muestre solo los registros cuyo lugar de origen sea diferente del valor p que se carga por teclado.
#
# 3- Buscar en el arreglo creado en el punto 1 un registro en el cual el número de identificación del artículo sea igual a num
# (cargar num por teclado).  Si existe, mostrar por pantalla todos los datos de ese registro.
# Si no existe, informar con un mensaje. La búsqueda debe detenerse al encontrar el primer registro
# que coincida con el patrón pedido.
#
# 4- A partir del arreglo, crear un archivo de registros en el cual se copien los datos de todos
# los registros cuyo tipo no sea igual al valor tip que se carga por teclado.
#
# 5- Mostrar el archivo creado en el punto anterior, a razón de un registro por línea en la pantalla.
# Muestre al final del listado dos líneas adicionales: una con la cantidad de registros que se mostraron,
# y otra con el precio de venta promedio de todos los registros que se mostraron.
import pickle

import registro

import os.path


def menu():
    print("1_Cargar registros")
    print("2_Mostrar registros")
    print("3_Buscar por ID")
    print("4_Generar archivos por tipo")
    print("5_Mostrar archivo y porcentaje de los articulos")
    op = int(input("Ingrese la opcion que desea elegir: "))
    return op


def validar_menor(men, mensaje):
    n = int(input(mensaje))
    while n <= men:
        print("Error, cargue un valor mayor a", men)
        n = int(input(mensaje))
    return n


def insertar_en_orden(v, articulo):
    n = len(v)
    izq, der = 0, n - 1
    pos = 0
    while izq <= der:
        c = (izq + der) // 2
        if v[c].ide == articulo.ide:
            pos = c
            break
        elif articulo.ide > v[c].ide:
            izq = c + 1
        else:
            der = c - 1
    if izq > der:
        pos = izq
    v[pos:pos] = [articulo]


def cargar_registro(n):
    v = []
    for i in range(n):
        articulo = registro.generar_random()
        insertar_en_orden(v, articulo)
    return v


def mostrar_registros(v, p):
    for articulo in v:
        if articulo.lugar != p:
            print(registro.to_string(articulo))


def buscar_por_id(v, num):
    n = len(v)
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if v[c].ide == num:
            return v[c]
        elif num > v[c].ide:
            izq = c + 1
        else:
            der = c - 1
    return None


def generar_archivo(v, tip, nombre_archivo):
    archivo = open(nombre_archivo, "wb")
    for i in range(len(v)):
        if v[i].tipo != tip:
            pickle.dump(v[i], archivo)
    archivo.close()


def mostrar_y_promediar_archivo(nombre_archivo):
    total = total_venta = 0
    if os.path.exists(nombre_archivo):
        size = os.path.getsize(nombre_archivo)
        archivo = open(nombre_archivo, "rb")
        while archivo.tell() < size:
            articulo = pickle.load(archivo)
            print(registro.to_string(articulo))
            total += 1
            total_venta += articulo.precio
        archivo.close()
    else:
        print("El archivo no existe")
    return total, total_venta


def validar_entre(men, may, mensaje):
    n = int(input(mensaje))
    while men > n or n > may:
        print("Error, ingrese un valor entre", men, "y", may)
        n = int(input(mensaje))
    return n


def principal():
    v = []
    op = -1
    while op != 6:
        op = menu()
        if op == 1:
            n = validar_menor(0, "Ingrese cuantos articulos desea cargar: ")
            v = cargar_registro(n)
            print("Articulos cargados.")
        elif len(v) == 0 and op != 6:
            print("Cargue primero los articulos.")
        elif op == 2:
            p = validar_entre(0, 24, "Ingrese un lugar de origen que desea que se ignore al mostrar los articulos: ")
            mostrar_registros(v, p)
        elif op == 3:
            num = validar_menor(0, "Ingrese la ID del articulo que desea buscar: ")
            ide_encontrado = buscar_por_id(v, num)
            if ide_encontrado is None:
                print("Articulo no encontrado.")
            else:
                print("Articulo encontrado:")
                print(registro.to_string(ide_encontrado))
        elif op == 4:
            tip = validar_entre(0, 29, "Ingrese el tipo de los articulo que no desea cargar en el archivo: ")
            nombre_archivo = "articulos.dat"
            generar_archivo(v, tip, nombre_archivo)
            print("Archivo creado.")
        elif op == 5:
            nombre_archivo = "articulos.dat"
            total, total_venta = mostrar_y_promediar_archivo(nombre_archivo)
            if total == 0:
                print("No hay articulos con esas caracteristicas")
            else:
                print("Se mostraron", total, "articulo(s).")
                promedio = round(total_venta / total, 2)
                print("El precio de venta promedio de todos los articulos mostrados es: $", promedio)


if __name__ == '__main__':
    principal()
