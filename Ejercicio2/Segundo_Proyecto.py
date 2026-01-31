nombre = input("Dime tu nombre: ")
ganancias = input("Dime tus ganancias: ")

ganancias= int(ganancias)
comision = 13
resultado = ganancias*comision/100
print(round(resultado,2) + ganancias)


nombre = input("Dime tu nombre: ")
ganancias = input("Dime tus ganancias: ")

ganancias = int(ganancias)
comision = ganancias * 13 / 100
comision = round(comision,2)

print(f"Hola {nombre}, tus comisiones ascienden a: {comision} €")