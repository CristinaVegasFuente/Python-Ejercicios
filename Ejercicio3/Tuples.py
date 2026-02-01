# Creamos una tupla con varios números
mi_tuple = (1, 2, 3, 4)

# Comprobamos el tipo (tuple)
print(type(mi_tuple))

# Tupla con distintos tipos de datos
t = (1, 2.1, 5, 7)

# Accedemos al elemento en la posición 1
# (empieza a contar desde 0)
print(t[1])

# Tupla con otra tupla dentro (tupla anidada)
posicion = (1, 2, 3, (20, 15, 10), 4, 5, 6)

# Accedemos al elemento 15:
# primero entramos a la tupla interna [3]
# luego al índice [1]
print(posicion[3][1])

# Convertimos la tupla en lista (casting)
castin = list(posicion)

# Comprobamos el nuevo tipo (list)
print(type(castin))

# Creamos una tupla sencilla
tuple = (1, 2, 3)

# Desempaquetado de tuplas:
# cada variable se queda con un valor
x, y, z = tuple
print(x, y, z)

# len() → número de elementos de la tupla
print(len(tuple))

# count() → cuántas veces aparece el valor 1
print(tuple.count(1))

# index() → posición donde aparece el valor 3
print(tuple.index(3))
