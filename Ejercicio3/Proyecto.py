texto = ("""El cambio climático es uno de los mayores desafíos ambientales de nuestro tiempo, "
         ya que provoca un aumento progresivo de la temperatura media del planeta. 
         Este fenómeno está estrechamente relacionado con las actividades humanas, especialmente 
         la quema de combustibles fósiles y la deforestación. Como consecuencia, 
         se producen eventos climáticos extremos como olas de calor, sequías e inundaciones. 
         Además, el deshielo de los polos y glaciares contribuye a la subida del nivel del mar. 
         Afrontar el cambio climático requiere un compromiso global para reducir las emisiones 
         y proteger el medio ambiente.""")
#primero lo paso a minusculas
parrafo = texto.lower()
print(parrafo)
#convierto el texto en una lista de palabras
lista = texto.split()
print(lista)
#cuento cuantas palabras hay
print(len(lista))
#cual es la primera palabra y cual es la ultima
primera = lista [0]
ultima = lista [-1]
print(primera)
print(ultima)
#texto invertido
lista.reverse()
print(lista)
#convierto el texto en una lista de palabras
lista = texto.split()
print(lista)
#bueno a rehacer el texto con espacios intermedios
espacios = " ".join(lista)
print(espacios)
#se encuentra la palabra Python?
palabra = texto.find("python")
print(palabra)
print("python" in texto)
