# Creamos un texto (string)
mi_texto = "Esta es una prueba"

# Accedemos a caracteres usando índices POSITIVOS
# OJO: los strings empiezan en el índice 0
resultado = mi_texto[0]   # E
print(resultado)

resultado1 = mi_texto[1]  # s
print(resultado1)

resultado2 = mi_texto[2]  # t
print(resultado2)

resultado3 = mi_texto[3]  # a
print(resultado3)

resultado4 = mi_texto[4]  # espacio
print(resultado4)

# Accedemos a caracteres usando índices NEGATIVOS
# Se empieza a contar desde el final del texto
resultado6 = mi_texto[-6]
print(resultado6)

resultado7 = mi_texto[-5]
print(resultado7)

resultado8 = mi_texto[-4]
print(resultado8)

resultado9 = mi_texto[-3]
print(resultado9)

resultado10 = mi_texto[-2]
print(resultado10)

resultado11 = mi_texto[-1]  # último carácter
print(resultado11)

# Separador visual para que no se mezcle todo
print("-*-*-*-")

# index() devuelve el índice de la primera aparición del carácter
# Si NO lo encuentra → ERROR
resultado12 = mi_texto.index("n")
print(resultado12)

print("-*-*-*-")

# index() también puede empezar a buscar desde una posición concreta
resultado13 = mi_texto.index("a", 0)
print(resultado13)

print("-*-*-*-")

# index() buscando entre un rango de posiciones
resultado14 = mi_texto.index("a", 0, 18)
print(resultado14)

print("-*-*-*-")

# Ejercicio práctico con una frase larga
print(
    "Encuentra y muestra en pantalla el índice de la primera aparición "
    "de la palabra -práctica- en la siguiente frase"
)

frase = (
    "En teoría, la teoría y la práctica son los mismos. "
    "En la práctica, no lo son."
)

# find() devuelve el índice de la primera aparición
# Si NO lo encuentra → devuelve -1 (no peta)
resultado15 = frase.find("práctica")
print(resultado15)

print(
    "Encuentra y muestra en pantalla el índice de la última aparición "
    "de la palabra -práctica-"
)

# find() empezando a buscar desde una posición concreta
# (aquí se usa un índice avanzado para pillar la segunda aparición)
resultado16 = frase.find("práctica", 57)
print(resultado16)
