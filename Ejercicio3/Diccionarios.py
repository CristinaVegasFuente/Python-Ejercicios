# Creamos un diccionario simple con 3 claves y sus valores
diccionario = {'c1':'valor1', 'c2':'valor2', 'c3':'valor3'}

# Mostramos todo el diccionario por pantalla
print(diccionario)

# Guardamos en una variable el valor asociado a la clave 'c1'
r = diccionario['c1']

# Mostramos ese valor (en este caso 'valor1')
print(r)

# Creamos otro diccionario con datos de una persona
mi_dic = {
    "nombre": "Karen",
    "apellido": "Jurgens",
    "edad": 35,
    "ocupacion": "Periodista"
}

# Actualizamos el diccionario:
# - cambiamos edad y ocupación
# - añadimos una nueva clave llamada 'pais'
# OJO: usamos update, no recreamos el diccionario
mi_dic.update({
    "nombre": "Karen",
    "apellido": "Jurgens",
    "edad": 36,
    "ocupacion": "Editora",
    "pais": "Colombia"
})

# Diccionario más complejo:
# tiene diccionarios dentro y una lista dentro del diccionario
mi_dict = {
    "valores_1": {"v1": 3, "v2": 6},
    "puntos": {
        "points1": 9,
        "points2": [10, 300, 15]
    }
}

# Accedemos al segundo valor de la lista points2 (índice 1)
print(mi_dict["puntos"]["points2"][1])

# Volvemos a crear el diccionario mi_dic desde cero
mi_dic = {
    'nombre': 'Karen',
    'apellido': 'Jurgens',
    'edad': 35,
    'ocupacion': 'Periodista'
}

# Mostramos el diccionario final
print(mi_dic)
