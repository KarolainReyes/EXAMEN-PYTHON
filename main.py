from menu import*
from funciones import*

while True:
    op = menu_principal()
    match op:
        case "1":
                info_artista()
        case "2":   
                info_paises()
                fun_paises()
        case "3":
                info_genre()
                fun_genre()
        case "4":
                print("Generar un informe")
        case "5":
                mod_reportes()
        case "6":
                print("Saliendo del sistema")
                break   
        case _:
            print("Ingrese una opcion valida")