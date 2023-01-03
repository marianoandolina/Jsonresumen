import json  # Importa el framework json para que podamos trabajar con el y sus metodos

# Creamos los datos en formatos json

json_2 = {
    "name":"Mariano", 
    "lastname":"Andolina",
    "hijos": [
        {
        "name": "Oriana",
        "age": 8
        }
        ]
    }

# Accedemos a a los datos 

print(json_2["hijos"])  # Accedemos a al name hijos que contiene una lista
print(json_2["hijos"][0])  # Accedemos a la primera posicion de la lista
print(json_2["hijos"][0]["age"])  # Y accedemos al name "age" para que nos muestre el valor que contiene, que en este caso seria 8

"""
Si construimos a mano una variable con datos json, Python lo va a tomar como que es un diccionario entonces
tenemos que transformarlo a un json (serializar) con el metodo Dumps incluido en la libreria json
"""
# Vamos a verificar que tipo de dato tenemos en la variable que creamos al principio llamada json_2
print(type(json_2)) # Muestra <class 'dict'> indicando que es un diccionario de Python

# Realizando el dump o serializacion para transformar los datos a datos json
# Si solo lo transfromamos de la siguiente forma | json_2_transformado = json.dumps(json_2) | al hacer print muestra los datos como si fuera un diccionarios
# La manera correcta de realizar el dumps es agregarle el parametro indent
json_2_transformado = json.dumps(json_2, indent=4) 
# Al agregarle el indent cuando hacemos el print muestra la informacion como un json
# El indent es 4 porque corresponden a los 4 espacios por defectos de la indentacion en python

print(json_2_transformado) #  Mostramos el archivo con formato json identado

# Verificamos que tipo de datos es json_2_transformado, tendria que decirnos que es del tipo "str"
print(type(json_2_transformado)) # Muestra <class "str">

# No va a decir json, dice str porque el metodo dumps lo transforma a un json string

