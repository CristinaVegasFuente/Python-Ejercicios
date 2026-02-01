# String con todo el abecedario (incluida la Ñ)
texto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

# Slicing completo:
# [inicio : fin : paso]
# Aquí cogemos todo el texto tal cual
resultado = texto[0:27:1]
print(resultado)

# [::-1] → truco clásico para darle la vuelta al string
resultado1 = texto[::-1]
print(resultado1)

# Desde el índice 2 hasta el final, saltando de 2 en 2
resultado2 = texto[2:27:2]
print(resultado2)

# Cogemos solo las tres primeras letras
resultado3 = texto[0:3]
print(resultado3)

# Cogemos las letras finales (índices 24 a 26)
resultado4 = texto[24:27]
print(resultado4)

# String normal
mi_variable = "esta palabra será extraida"

# Extraemos la palabra "palabra"
# Índice 5 hasta 12 (el final no se incluye)
r = mi_variable[5:12]
print(r)

# Nueva frase (con tilde)
mi_variable = "esta palabra será extraída"

# Extraemos la palabra "será"
re = mi_variable[13:17]
print(re)
