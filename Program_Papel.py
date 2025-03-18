import os
from unidecode import unidecode
import re
import datetime as dt ##QUITAR SI NO SE VA A USAR
from tabulate import tabulate
import sqlite3
from sqlite3 import Error
import sys
import pandas as pd ##QUITAR SI NO SE VA A USAR

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def guiones_separadores():
    return print('-' * 50)

def guiones(longitud):
    return '-' * longitud

def aviso(mensaje, longitud):
    print(f"\n{guiones(longitud)} {mensaje} {guiones(longitud)}\n".upper()) 

def indicarEnter():
    input("\n\nDe clic en Enter para continuar.")

def fechaActual(): ##QUITAR SI NO SE VA A USAR
    fecha_actual = dt.date.today()
    return fecha_actual

def darFormatoATexto(texto, eliminarNumeros = False, eliminarCaracteresEspeciales = False):
    if eliminarNumeros:
        texto = re.sub(r'\d', '', texto)

    if eliminarCaracteresEspeciales:
        texto = re.sub(r'[^A-Za-z0-9 ]', '', texto)

    texto = unidecode(texto).strip().upper()
    texto = re.sub(r'\s+', ' ', texto)

    return texto

def validarUnicamenteTexto(texto):
    if texto.replace(' ', '').isalpha():
        return True
    return False

def solicitarSoloNumeroEntero(descripcion):
    while True:
        respuesta = input(f"{descripcion}: ")

        if respuesta.isdigit():
            return int(respuesta)
        else:
            print("\nIngrese un número válido.")

def respuestaSINO():
    while True:
        respuesta = darFormatoATexto(input('\tRespuesta: '))

        if respuesta == 'SI' or respuesta == 'NO':
            break
        else:
            print('\n\tIngrese una respuesta válida (Sí/No).')
    return respuesta

def validarContinuarOpcion():
    continuarOpcion = None
    while continuarOpcion != "0" and continuarOpcion != "":
        continuarOpcion = input(f"Pulse Enter para continuar la opción actual o ingrese 0 para volver al menú anterior. ").strip()
    if continuarOpcion == "0":
        return True
    else:
        print("\n")
    
def validarOpcionesNumericas(opcionMin, opcionMax):
    while True:
        try:
            opcionValida = int(input(f"Opción: "))
            if opcionValida >= opcionMin and opcionValida <= opcionMax:
                return opcionValida
            else:
                print(f"\nIngrese un número válido ({opcionMin}-{opcionMax}).")
        except ValueError:
            print(f"\nIngrese un número válido ({opcionMin}-{opcionMax}).")

def contarCantidadOpcionesDeMenu(listaActual):
    cantidad = len(listaActual) - 1
    return cantidad

def mostrarOpcionesDeMenu(listaActual):
    print('Ingrese el número de la opción que desee realizar:')
    print(tabulate(listaActual, headers = 'firstrow', tablefmt = 'pretty'))

def mostrarYValidarMenu(ubicacion, opcion, lista):
    mostrarTitulo(ubicacion, True)
    
    mostrarOpcionesDeMenu(lista)

    opcion = validarOpcionesNumericas(1, contarCantidadOpcionesDeMenu(lista))

    limpiar_consola() 
    
    if not opcion == contarCantidadOpcionesDeMenu(lista):
            ubicacion.append(lista[opcion][1])

    return opcion, ubicacion

def mostrarTitulo(ubicacion, esMenu = False):
    print(f'Ubicación: {" / ".join(ubicacion)}')
    
    if esMenu == True:
        aviso(f'MENÚ {ubicacion[-1]}', 20)
    
    else:
        aviso(f'{ubicacion[-1]}', 20)
        return

def desplegar_menu():
    print("Menu de Opciónes")
    print("1. Realizar venta")
    print("2. Inventario")
    print("3. Alta a clientes")
    print("4. Pedido a proveedor")
    print("5. Alta a proveedores")
    print("6. Sair")
    opcion = int(input("Seleccione una opción: "))
    return opcion

def menu():
    while True:
        try:
            limpiar_consola()
            opcion = desplegar_menu()
            if opcion == 1:
                print("Realizar venta.")
                x = input("Presiona Enter para continuar...")
            elif opcion == 2:
                print("Inventario.")
                x = input("Presiona Enter para continuar...")
            elif opcion == 3:
                print("Alta a clientes.")
                x = input("Presiona Enter para continuar...")
            elif opcion == 4:
                print("Pedido a proveedor.")
                x = input("Presiona Enter para continuar...")
            elif opcion == 5:
                print("Alta a proveedor.")
                x = input("Presiona Enter para continuar...")
            elif opcion == 6:
                print("Saliendo...")
                break
            else:
                print("Opción no válida, intenta nuevamente.")
        except ValueError:
            print("Por favor, ingresa un número válido.")



try:
    with sqlite3.connect('SISTEMA_VENTA_PAPELERIA.db') as conn:
        mi_cursor = conn.cursor()
        mi_cursor.execute("CREATE TABLE IF NOT EXISTS CLIENTES\
                        (ID_CLIENTE INTEGER PRIMARY KEY NOT NULL, NOMBRE TEXT NOT NULL,\
                        APELLIDO TEXT NOT NULL, TELEFONO INT NOT NULL, EMAIL TEXT NOT NULL);")

        mi_cursor.execute("CREATE TABLE IF NOT EXISTS DETALLES_VENTAS\
                        (ID_DETALLEVENTA INTEGER PRIMARY KEY NOT NULL,\
                        CANTIDAD INTEGER NOT NULL, PRECIO_UNIT INT NOT NULL, ID_CLIENTE INTEGER NOT NULL,\
                        FOREIGN KEY (ID_CLIENTE) REFERENCES CLIENTES(ID_CLIENTE));")
        
        mi_cursor.execute("CREATE TABLE IF NOT EXISTS VENTAS\
                        (ID_VENTA INTEGER PRIMARY KEY NOT NULL, FECHA timestamp NOT NULL,\
                        TOTAL INTEGER NOT NULL, ID_DETALLEVENTA INTEGER NOT NULL,\
                        FOREIGN KEY (ID_DETALLEVENTA) REFERENCES DETALLES_VENTAS(ID_DETALLEVENTA));")
        
        mi_cursor.execute("CREATE TABLE IF NOT EXISTS CATEGORIAS\
                        (ID_CATEGORIA INTEGER PRIMARY KEY NOT NULL,\
                        NOMBRE TEXT NOT NULL);")

        mi_cursor.execute("CREATE TABLE IF NOT EXISTS PROVEEDORES \
                        (ID_PROVEEDOR INTEGER PRIMARY KEY NOT NULL, NOMBRE TEXT NOT NULL, DIRECCION TEXT NOT NULL,\
                        TELEFONO INT NOT NULL, EMAIL TEXT NOT NULL);")

        mi_cursor.execute("CREATE TABLE IF NOT EXISTS COMPRAS\
                        (ID_COMPRA INTEGER PRIMARY KEY NOT NULL, FECHA timestamp NOT NULL,\
                        TOTAL INT NOT NULL,CANTIDAD INTEGER NOT NULL, ID_PROVEEDOR INTEGER NOT NULL,\
                        FOREIGN KEY (ID_PROVEEDOR) REFERENCES PROVEEDORES(ID_PROVEEDOR));")

        mi_cursor.execute("CREATE TABLE IF NOT EXISTS PRODUCTOS \
                        (ID_PRODUCTO INTEGER PRIMARY KEY NOT NULL,\
                        NOMBRE TEXT NOT NULL,\
                        DESCRIPCION TEXT NOT NULL,\
                        PRECIO INT NOT NULL,\
                        STOCK INT NOT NULL,\
                        ID_VENTA INTEGER PRIMARY KEY NOT NULL, \
                        ID_CATEGORIA INTEGER PRIMARY KEY NOT NULL,\
                        ID_COMPRA INTEGER PRIMARY KEY NOT NULL, \
                        FOREIGN KEY (VENTA) REFERENCES VENTAS(VENTA),\
                        FOREIGN KEY (ID_CATEGORIA) REFERENCES CATEGORIAS(ID_CATEGORIA)\
                        FOREIGN KEY (ID_COMPRA) REFERENCES COMPRAS(ID_COMPRA));")
            
        print(f'{guiones(17)}Tablas creadas o cargadas exitosamente.{guiones(17)}')
except Error as e:
    print(e)
except Exception:
    print(f'Se produjo el siguiente error {sys.exc_info()[0]}')
finally:
    conn.close()


menu()
