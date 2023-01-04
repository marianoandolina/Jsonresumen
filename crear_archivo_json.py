import json

def json_serialize():

    # Creamos una variable con datos tipo json {name:value} 
    # Si nos fijamos en donde esta el name:"materias" es una lista dentro de un diccionario.   

    estudiante1 = {
                  "nombre": "Max",
                  "apellido": "Power",
                  "materias": [
                      {
                       "asignatura": "matematica",
                       "estado": "en curso"
                      },
                      {
                       "asignatura": "lengua",
                       "estado": "finalizado"
                      }
                      ]
                   }


# Transfromamos el diccionario de la variable estudiante1 a datos jston string y creamos el archivo

    with open('estudiantes.json', 'w') as jsonfile:  # Creamos el archivo 'estudiantes.json' con el modo 'w' (escribe el archivo)
        data = [estudiante1] # La data que le pasamos tiene que estar en formato lista por eso es que le colocamos los corchetes
        json.dump(data, jsonfile, indent=4) 

        # data es donde estan los datos
        # jsonfile es donde van a ir esos datos para escribirse en el archivo
        # indent=4 el la identacion para que quede todo en formato json

    # Podemos ver en el explorador de la izquierda que se creo el archivo mi_family.json con los datos de la variable family

def json_deserialize():
    
    # Leer json y actualizarlo
    # Cargamos la data en una variable con formato diccionario

    estudiante2 = {
                  "nombre": "Jean",
                  "apellido": "Gray",
                  "materias": [
                      {
                       "asignatura": "matematica",
                       "estado": "finalizado"
                      },
                      {
                       "asignatura": "lengua",
                       "estado": "finalizado"
                      }
                      ]
                   }

    # Leemos el archivo al cual le queremos agregar los datos 'mi_json.json' y se guardan en la variable temporal llamada jsonfile
    with open('estudiantes.json', 'r') as jsonfile: 
        
        # Deserializamos (pasar de json a dicc) con el metodo load los datos de la variable temporal jsonfile
        
        current_data = json.load(jsonfile)        
        # Al estar los datos en formato dicc le podemos agregar los datos que creamos nosotros en el mismo formato
        
        current_data.append(estudiante2) 
        # El metodo append agrega los datos creados a los datos leidos y deserializados del archivo

    # Volvemos a crear el archivo y con el metodo dump serializamos los datos unificados.
    with open('estudiantes.json', 'w') as jsonfile:
        json.dump(current_data, jsonfile, indent=4)

    # A modo de prueba volvemos a leer lo que tiene el archivo 'mi_json.json' ahora, lo deserializamos con el metodo load
    with open('estudiantes.json', 'r') as jsonfile:
        json_data = json.load(jsonfile)

    print('Mostrar el contenido del archivo mi_json')
    # En una sola linea serializamos los datos y los mostramos en formato json.
    print(json.dumps(json_data, indent=4)) 


if __name__ == '__main__':

    json_serialize()
    json_deserialize()
