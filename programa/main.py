import funcion
import basedatos
import lista

from tabulate import tabulate

def ejecutarMenu(ubicacion, opcion, lista):
    ubicacionTitulo(ubicacion)
    mostrarOpciones(lista)
    opcion = recibirInfo(lista)
    if not opcion == contarLista(lista):
            ubicacion.append(lista[opcion][1])

def ubicacionTitulo(ubicacion):
    print(f'Ubicación: {" / ".join(ubicacion)}')
    print(f'MENÚ {ubicacion[-1]}', 20)
    
def mostrarOpciones(listaActual):
    print('Ingrese el número de la opción que desee realizar:')
    print(tabulate(listaActual, headers = 'firstrow', tablefmt = 'pretty'))

def recibirInfo(listaActual):
    opcion = funcion.solicitarRangoEntero(1, contarLista(listaActual))
    return opcion

def contarLista(listaActual):
    cantidad = len(listaActual) - 1
    return cantidad

def menu():
    while True:
        try:
            opcion = 1
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


"""
def menuPrincipal():
    opcion = 0

    while True:
        #ubicacion = ['Menú principal']
        if opcion == 0:
            print('PUNTO DE VENTA')
            print('¡Bienvenido al menú principal!\n')
            mostrarOpcionesDeMenu(lmenu_principal)

            opcion = validarOpcionesNumericas(1, contarCantidadOpcionesDeMenu(lmenu_principal))

        if not opcion == contarCantidadOpcionesDeMenu(lmenu_principal):
            ubicacion.append(lmenu_principal[opcion][1])
            limpiar_consola()

        if opcion == 1:
            menuNotas(ubicacion)

        elif opcion == 2:
            menuClientes(ubicacion)            

        elif opcion == 3:
            menuServicios(ubicacion)

        elif opcion == 4:
            menuEstadisticas(ubicacion)
        
        else:
            print('\n¿Está seguro que desea salir? (Sí/No)')
            respuesta = respuestaSINO()

            if respuesta == 'SI':
                aviso("Archivo cerrado correctamente.", 25)
                aviso("Gracias por usar nuestro sistema, hasta la próxima.", 15)
                break
            else:
                limpiar_consola()
                opcion = 0

        opcion = 0
        continue"""

def menuPrincipal(ubicacion):
    ubicacionOriginal = ubicacion.copy()
    opcion = 0

    while True:    
        ubicacion = ubicacionOriginal.copy()
        if opcion == 0:
            opcion, ubicacion = ejecutarMenu(ubicacion, opcion, lista.ls_menuPrincial)

        if opcion == 1:
            input("Presiona Enter para continuar...")

        elif opcion == 2:
            input("Presiona Enter para continuar...")

        elif opcion == 3:
            input("Presiona Enter para continuar...")

        else:
            break

        opcion = 0
        funcion.limpiar_consola()
        continue

basedatos.creacionBaseDeDatos()
menuPrincipal()