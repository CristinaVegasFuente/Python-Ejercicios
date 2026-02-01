# Creamos dos strings
v1 = "cris"
v2 = "tina"

# Concatenamos (unimos) strings con +
print(v1 + v2)   # "cristina"

# Repetimos el string 10 veces con *
print(v1 * 10)

# String multilínea usando triple comillas
frase = """me gusta cuando callas
porque estas como ausente
asi que silencio, por favor"""

# Mostramos todo el texto tal cual
print(frase)

# Comprobamos si una palabra está dentro del texto
# Devuelve True si está, False si no
print("silencio" in frase)
print("silencio" not in frase)

print("sol" in frase)
print("sol" not in frase)

# String con símbolos incluidos
palabras = "¡¡¡Hola mundo!!!"

# len() cuenta TODOS los caracteres (letras, espacios y símbolos)
print(len(palabras))



