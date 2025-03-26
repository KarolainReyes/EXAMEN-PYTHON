#LimeWire desea implementar un sistema integral de gestión que permita manejar todas las operaciones relacionadas con la administración de datos de artistas·
#musicales, países, géneros musicales, así como la generación de informes relevantes.

def menu_principal():
    menuPrincipal= """
******************LimeWire******************
**Bienvenido al sistema de Gestion Musical**
********************************************
Por favor seleccione la opcion que desea:

1. Registrar informacion de un artista
2. Informacion sobre paises
3. Informacion sobre generos musicales
4. Generar un informe
5. Abrir "Modulo de Reportes"
6. Salir del sistema
********************************************
"""
    print(menuPrincipal)
    return input("Ingrese su opcion: ")

def info_paises():
    infoPaises= """
******************LimeWire******************
******Bienvenido a la Gestion de Paises*****
Por favor selecione la opcion que desea:

1. Regitrar un Pais
2. Ver Paises registrados
3. Buscar un Pais
4. Salir del sistema
********************************************
"""
    print(infoPaises)
    return input ("Ingrese su opcion: ")

def info_genre():
    infoGenero= """
******************LimeWire******************
******Bienvenido a la Generos Musicales*****
Por favor selecione la opcion que desea:

1. Registar un genero musical
2. Ver generos musicales registrados
3. Buscar un genero musical
4. Salir del sistema
"""
    print(infoGenero)
    return input("Ingrese su opcion: ")

def mod_reportes():
    modReportes= """
******************LimeWire******************
******Bienvenido al Modulo de Reportes******
********************************************
Por favor selecione la opcion que desea:

1. Ver los datos de artistas musicales para Reino Unido desde 1960 hasta 1970.
2. Datos de artistas musicales para el género Rock/pop
3. Datos de artistas musicales el los ultimos diez anios
4. Numero de artistas registrados por anio
5. Unidades certificadas totales registradas para todos los países en 2023.
6. Salir del sistema.
"""
    print(modReportes)
    return input("Ingrese su opcion: ")

