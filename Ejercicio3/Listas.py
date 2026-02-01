# Creamos una lista con letras
mi_lista = ['a', 'b', 'c']

# Mostramos el tipo de la variable (es una lista)
print(type(mi_lista))

# Lista mezclando tipos: string, entero y float (Python lo permite)
otra_lista = ['hola', 55, 6.1]

# Mostramos la lista completa
print(otra_lista)


# Nueva lista con más letras
lista = ['d', 'f', 'g']

# len() devuelve cuántos elementos tiene la lista
r = len(lista)

# Hacemos un slicing desde el inicio hasta el final (copia de la lista)
re = lista[0:]

# Mostramos la longitud
print(r)

# Unimos dos listas con el +
lista3 = mi_lista + lista

# Cambiamos el primer elemento de la lista (las listas SÍ son modificables)
lista3[0] = 'alfa'

# Añadimos un nuevo elemento al final
lista3.append('h')

# Mostramos la lista resultante
print(lista3)

# Creamos otra lista
lista4 = ['i', 'j', 'k']

# pop() elimina el último elemento de la lista
lista4.pop()

# Mostramos la lista sin el último elemento
print(lista4)

# Lista desordenada
lista5 = ['e', 'c', 'a', 'f', 'b', 'd']

# sort() ordena la lista alfabéticamente
lista5.sort()
print(lista5)

# reverse() le da la vuelta al orden de la lista
lista5.reverse()
print(lista5)
