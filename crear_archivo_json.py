import json

# Creamos una variable con datos tipo json {name:value}
# Como es una lista de diccionarios comienza y cierra con []

family = [{
    "name":"Mariano", "age":39            
},
{
    "name":"Oriana", "age":8
},
{
    "name":"Myrian", "age":47
}]    


# Transfromamos el diccionario de la variable family a datos jston string y creamos el archivo

with open('mi_family', 'w') as jsonfile:
    json.dump(family, jsonfile, indent=4) 

# Podemos ver en el explorador de la izquierda que se creo el archivo mi_family.json con los datos de la variable family


    


 
