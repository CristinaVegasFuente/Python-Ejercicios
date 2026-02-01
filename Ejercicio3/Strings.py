# Creamos un texto (string)
texto = "Este es el texto de prueba de CRISTINA VEGAS FUENTE"

# upper() → pone TODO el texto en mayúsculas
r = texto.upper()
print(r)

# lower() → pone TODO el texto en minúsculas
re = texto.lower()
print(re)

# split() sin parámetros → separa el texto por espacios
res = texto.split()
print(res)

# split("t") → corta el texto cada vez que encuentra una 't' minúscula
resu = texto.split("t")
print(resu)

# split("T") → lo mismo pero con 'T' mayúscula (no es lo mismo)
resul = texto.split("T")
print(resul)

# find() → devuelve el índice de la primera 's'
# Si no encuentra nada → devuelve -1
result = texto.find("s")
print(result)

# replace() → sustituye TODAS las 'e' minúsculas por 'x'
resulta = texto.replace("e", "x")
print(resulta)

# replace() → sustituye TODAS las 'E' mayúsculas por 'X'
resulta = texto.replace("E", "X")
print(resulta)

# Variables sueltas para luego unirlas
a = "Aprender"
b = "Python"
c = "es"
d = "genial"

# join() → une palabras usando el separador "-"
e = "-".join([a, b, c, d])
print(e)

# Lista de palabras
lista_palabras = ["La", "legibilidad", "cuenta."]

# join() con espacios para formar una frase
resultad = " ".join(lista_palabras)
print(resultad)

# Frase original
frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."

# replace() encadenado:
# cambiamos 'difícil' por 'fácil' y 'mala' por 'buena'
resultado = frase.replace("difícil", "fácil").replace("mala", "buena")
print(resultado)


