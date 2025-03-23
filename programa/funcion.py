import os
import datetime as dt

# FUNCIONES GENERALES.
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

# SOLICITAR DATOS.
def solicitarEntero(descripcion):
    while True:
        respuesta = input(f"{descripcion}: ")

        if respuesta.isdigit():
            return int(respuesta)
        else:
            print("\nIngrese un número válido.")

def solicitarRangoEntero(opcionMin, opcionMax):
    while True:
        try:
            opcionValida = int(input(f"Opción: "))
            if opcionValida >= opcionMin and opcionValida <= opcionMax:
                return opcionValida
            else:
                print(f"\nIngrese un número válido ({opcionMin}-{opcionMax}).")
        except ValueError:
            print(f"\nIngrese un número válido ({opcionMin}-{opcionMax}).")

# VALIDACIONES.
def validarSoloTexto(texto):
    if texto.replace(' ', '').isalpha():
        return True
    return False

def validarSoloNumeros(texto):
    if texto.replace(' ', '').isdigit():
        return True