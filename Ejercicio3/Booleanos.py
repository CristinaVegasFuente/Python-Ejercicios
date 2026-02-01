# Creamos dos variables booleanas (True y False de toda la vida)
var1 = True
var2 = False

# Vemos de qué tipo es var1 (spoiler: bool)
print(type(var1))

# Comparación: 5 es mayor que (2 + 3)?
# 2 + 3 = 5 → 5 > 5 es False
n = 5 > 2 + 3
print(n)

# Comparación de igualdad:
# 5 es igual a (2 + 3)?
# 2 + 3 = 5 → True
nu = 5 == 2 + 3
print(nu)

# Guardamos en 'prueba' el resultado de una comparación
# 6 es igual a (5 * 3)? → 6 == 15 → False
prueba = 6 == 5 * 3

# Comprobamos si una división es mayor que una multiplicación
# El resultado será True o False y lo mostramos
var = 17834 / 34 > 87 * 56
print(var)

# Creamos una lista de números
lista = [1, 2, 3, 4, 5]

# Comprobamos si el 6 NO está en la lista → True
control = 6 not in lista
print(control)

# Comprobamos si el 6 SÍ está en la lista → False
control2 = 6 in lista
print(control2)

# Comprobamos si la raíz cuadrada de 25 es igual a 5
# 25 ** 0.5 = 5 → True
print(25 ** 0.5 == 5)

# Recordatorio rápido:
# Operadores de comparación más usados:
# <   menor que
# >   mayor que
# ==  igual que
# !=  distinto de
