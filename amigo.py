nombre = input("Hola, ¿Cómo te llamas?")
print ("No me gusta tu nombre, ", nombre)

#interacción en la que se pide el nombre a la persona.

anos = float(input(f"¿Cuántos años tienes, {nombre} "))
if anos>70 : 
    print ("Te faltan 5 telediarios, encantado!!")
else :  print("Encantado de conocerte.")

#poniendo el if y el else para dar una reacción dependiendo de la edad metida.

mates = input(f"¿Se te dan bien las mates, {nombre}? ")
if mates == "si" or "Si" or "Sí" or "sí" or "yes" : #Se ponen las tantas opciones de respuesta para elaborar la respuesta
    print ("Perfecto, te voy a hacer una pregunta de una multiplicacoón que no se hacerla, ayúdame.")
else : print ("Tranquilo que la pregunta es fácil, podrás con ella.")
#dependiendo de la respuesta dada se darám 2 respuestas distintas.
pregunta = float(input("¿Cuánto es 2 + 3?"))
print (f"Pues por el culo te la hinco, espabila que me voy ya, {nombre} ")