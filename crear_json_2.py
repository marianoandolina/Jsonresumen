import json

""" Esta funcion lo que hace es crear un json pasando los datos que creamos nostros dentro de las variables.
Cada dato de las variables estan en formato json pero aun no fueron serializadas (transformadas a json), por ahora son diccionario
de Python """ 

def crear_familiares():

    mariano = {
        "name":"Mariano",
        "last_name":"Andolina",
        "age":"39",
        "sons": [
                {
                "firsname":"Brian",
                "age":21
                },
                {
                "firstname":"Oriana",
                "age":8
                }
                ]
    }

    oriana = {
        "name":"Oriana",
        "last_name":"Andolina",
        "age":8,
        "sons":[]
    }

    myrian = {
        "name":"Myrian",
        "last_name":"Rodriguez",
        "age":8,
        "sons": [
                {
                "name":"Oriana",
                "age":8
                }
        ]
    }

    json_test= {"mariano":mariano, "oriana": oriana, "myrian": myrian}

    print('Imprimir json como un objeto')
    print(mariano) # Muestra los datos json como un objeto comun de python o sea como un diccionario con listas anidadas

    json_string = json.dumps (mariano, indent=4)  # Transformamos los datos en la variable mariano a json strings con la identacion.

    print('Imprimir json como un string')
    print(json_string) # Mustra los datos de la variable mariano como json.

    json_test_dump = json.dumps(json_test, indent=4)
    print(json_test_dump)

if __name__ == "__main__":
    crear_familiares()


