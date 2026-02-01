# Creamos un set usando set() a partir de una tupla
mi_set = set((1, 2, 3, 4, 5, 6))

# Comprobamos el tipo (set)
print(type(mi_set))

# Mostramos el set
# OJO: los sets NO mantienen orden
print(mi_set)

# Creamos otro set directamente con llaves
otro_set = {1, 2, 3, 4, 5, 6, 7}

# Comprobamos el tipo
print(type(otro_set))

# Mostramos el set
print(otro_set)

# Creamos dos sets distintos
s1 = {1, 2, 3}
s2 = {4, 5, 6}

# Unimos ambos sets (sin duplicados)
s3 = s1.union(s2)

# Añadimos un elemento al set
# Si ya existiera, no pasa nada
s1.add(4)
print(s1)

# remove() elimina un elemento
# OJO: si no existe, da ERROR
s1.remove(3)
print(s1)

# discard() elimina un elemento
# Si no existe, NO da error (más seguro)
s1.discard(2)
print(s1)

# clear() vacía el set por completo
s1.clear()
print(s1)

# Set con nombres para un sorteo
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}

# pop() elimina un elemento ALEATORIO
# No sabes cuál va a salir
sorteo.pop()

# Sets pueden mezclar tipos de datos
mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}

# Union de sets (sin repetir valores)
mi_set_3 = mi_set_1.union(mi_set_2)

# Volvemos a crear el set del sorteo
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}

# Añadimos un nuevo nombre al set
sorteo.add("Damián")