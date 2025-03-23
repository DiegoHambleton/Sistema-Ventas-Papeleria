import sqlite3
from sqlite3 import Error
import sys

def creacionBaseDeDatos():
    try:
        with sqlite3.connect('BD_Papeleria.db') as conn:
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
            
            mi_cursor.execute("""CREATE TABLE IF NOT EXISTS PRODUCTOS (
                ID_PRODUCTO INTEGER PRIMARY KEY NOT NULL,
                NOMBRE TEXT NOT NULL,
                DESCRIPCION TEXT NOT NULL,
                PRECIO INT NOT NULL,
                STOCK INT NOT NULL,
                ID_VENTA INTEGER NOT NULL,
                ID_CATEGORIA INTEGER NOT NULL,
                ID_COMPRA INTEGER NOT NULL,
                FOREIGN KEY (ID_VENTA) REFERENCES VENTAS(ID_VENTA),
                FOREIGN KEY (ID_CATEGORIA) REFERENCES CATEGORIAS(ID_CATEGORIA),
                FOREIGN KEY (ID_COMPRA) REFERENCES COMPRAS(ID_COMPRA));""")
            print("Base de datos creada o cargada correctamente.")
    except Error as e:
        print("Ocurrió un error al crear la base de datos:")
        print(e)
    except Exception:
        print(f'Se produjo el siguiente error: {sys.exc_info()[0]}.')
    finally:
        conn.close()

def insertarDatos(tabla, datos):
    try:
        with sqlite3.connect('BD_Papeleria.db') as conn:
            mi_cursor = conn.cursor()
            mi_cursor.execute(f"INSERT INTO {tabla} VALUES ({datos});")
            conn.commit()
            print("Datos insertados correctamente.")
    except Error as e:
        print("Ocurrió un error al insertar los datos:")
        print(e)
    except Exception:
        print(f'Se produjo el siguiente error: {sys.exc_info()[0]}.')
    finally:
        conn.close()

def consultarDatos(tabla):
    try:
        with sqlite3.connect('BD_Papeleria.db') as conn:
            mi_cursor = conn.cursor()
            mi_cursor.execute(f"SELECT * FROM {tabla};")
            datos = mi_cursor.fetchall()
            print("Datos consultados correctamente.")
            return datos
    except Error as e:
        print("Ocurrió un error al consultar los datos:")
        print(e)
    except Exception:
        print(f'Se produjo el siguiente error: {sys.exc_info()[0]}.')
    finally:
        conn.close()

def actualizarDatos(tabla, columna, valor, condicion):
    try:
        with sqlite3.connect('BD_Papeleria.db') as conn:
            mi_cursor = conn.cursor()
            mi_cursor.execute(f"UPDATE {tabla} SET {columna} = {valor} WHERE {condicion};")
            conn.commit()
            print("Datos actualizados correctamente.")
    except Error as e:
        print("Ocurrió un error al actualizar los datos:")
        print(e)
    except Exception:
        print(f'Se produjo el siguiente error: {sys.exc_info()[0]}.')
    finally:
        conn.close()

def eliminarDatos(tabla, condicion):
    try:
        with sqlite3.connect('BD_Papeleria.db') as conn:
            mi_cursor = conn.cursor()
            mi_cursor.execute(f"DELETE FROM {tabla} WHERE {condicion};")
            conn.commit()
            print("Datos eliminados correctamente.")
    except Error as e:
        print("Ocurrió un error al eliminar los datos:")
        print(e)
    except Exception:
        print(f'Se produjo el siguiente error: {sys.exc_info()[0]}.')
    finally:
        conn.close()

def consultarDatosEspecificos(tabla, columna, condicion):
    try:
        with sqlite3.connect('BD_Papeleria.db') as conn:
            mi_cursor = conn.cursor()
            mi_cursor.execute(f"SELECT {columna} FROM {tabla} WHERE {condicion};")
            datos = mi_cursor.fetchall()
            print("Datos consultados correctamente.")
            return datos
    except Error as e:
        print("Ocurrió un error al consultar los datos:")
        print(e)
    except Exception:
        print(f'Se produjo el siguiente error: {sys.exc_info()[0]}.')
    finally:
        conn.close()