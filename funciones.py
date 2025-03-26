import json
from menu import*

global archivo_json, name_artistas
artistasjson="artistas.json"
paisesjson="paises.json"

def info_artista():
        global artistasjson
        with open (artistasjson, "r") as file:
            name_artistas = json.load (file)
        cname = input("Ingrese el nombre del artista: ")
        existe = False
        for x in name_artistas:
          for cod in x.values():
            if cod == cname:
             existe = True
            
        if existe == True:
            print("Este artista ya está registrado en la base de datos")
        else:
            
            pais_origen=input("Ingrese el pais de origen de este artista: ")
            actividad=int(input("Ingrese los anios de actividad en la industria de este artista: "))
            prim_disco=int(input("Ingrese el anio de lanzamiento de su primer disco: "))
            genre=input("Ingrese el/los genero(s) musicales: ")
            total_certf=(input("Ingrese el total de unidades Certificadas: "))
            ventas_recla=(input("Ingrese el total de ventas reclamadas: "))
            estado= False
            newartist= {"Country": pais_origen,
                        "Active years": actividad,
                        "Release year of first charted record": prim_disco,
                        "Genre": genre,
                        "Total certified units": total_certf,
                        "Claimed sales": ventas_recla,
                        "Estado": estado
    }

            name_artistas.append(newartist)
            with open("artistas.json", "w") as file:
                json.dump(name_artistas, file, indent=4)
                print("Artista registrado con éxito!")
                
def leerjson():
    global archivo_json
    with open (archivo_json, "r") as file:
             pr=json.load(file)
    return pr


archivo_json = "artistas.json"
artistasReg=leerjson()

def fun_paises():
    while True:
        op = info_paises()
        match op:
            case "1":
                    print("Registrar un pais")
            case "2":   
                    print("ver paises registrados")
            case "3":
                    print("buscar un pais")
            case "4":
                    print("saliendo")
                    break 
            case _:
                    print("Ingrese una opcion valida")

def fun_genre():
     while True:
        op = info_genre()
        match op:
            case "1":
                    print("Registrar un genero musical")
            case "2":   
                    print("ver generos musicales registrados")
            case "3":
                    print("buscar un genero musical")
            case "4":
                    print("saliendo")
                    break 
            case _:
                    print("Ingrese una opcion valida") 

def registrar_pais():
        global paisesjson
        with open (paisesjson, "r") as file:
            paises_reg = json.load (file)
        pais = input("Ingrese el pais a registrar: ")
        existe = False
        for x in paises_reg:
          for cod in x.values():
            if cod == pais:
             existe = True
            
        if existe == True:
            print("Este Pais ya está registrado en la base de datos")
        else:
            
            codigo_ISO=input("Ingrese el codigo ISO del pais: ")
            codigo_ISO3=input("Ingrese el codigo ISO3 del pais: ")
            newcontry= {"Codigo ISO": codigo_ISO,
                        "Codigo ISO 3" : codigo_ISO3
    }

            paises_reg.append(newcontry)
            with open("artistas.json", "w") as file:
                json.dump(paises_reg, file, indent=4)
                print("Pais registrado con éxito!")
            
