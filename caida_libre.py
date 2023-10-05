altura_i = float(input("altura inicial: "))
# se pide la altura inicial ya que se necesita en la formula de caída libre.
gravedad = float(input("La gravedad: ")) 
# Se piede la gravedad pues es un valor que se necesita en la formla de caída libre.
tiempo = float(input("Introduce el tiempo en el cual quieres calcular su posición: "))
#Se pide el tiempo pues dependiendo del tiempo que se ponga la posición varía.
velocidad = float(input("La velocidad es: "))
#Se pide la velocidad pues en la formula esta multiplica al tiempo y dependiendo de esta varía el resultado final.
posicion = velocidad*tiempo-(1/2)*gravedad*tiempo*tiempo+altura_i
#Se calcula la posición usando los valores pedidos previamente.
print ("La posición (h) es: ", posicion)